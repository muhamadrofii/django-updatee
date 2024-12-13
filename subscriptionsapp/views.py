from django.shortcuts import render
import uuid
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from .models import Transaction, Subscription
from midtransclient import Snap, CoreApi
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
import time

# Create your views here.
def langganan(request):
    return render(request, 'formLangganan.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def create_payment_link(request):
    if request.method == 'POST':
        # Ambil data dari dropdown
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        plan = request.POST.get('plan')

        # Validasi input plan
        if plan not in ['basic', 'premium', 'ultimate']:
            return JsonResponse({'error': 'Invalid plan selected'}, status=400)

        # Tentukan harga berdasarkan plan yang dipilih
        plan_prices = {
            'basic': 29000,
            'premium': 99000,
            'ultimate': 199000
        }
        amount = plan_prices[plan]

        # Ambil data pengguna langsung dari model User
        if request.user.is_authenticated:
            # fullname = f"{request.user.first_name} {request.user.last_name}"
            email = email or request.user.email  # Use form email if available
            phone = phone or getattr(request.user, 'phone_number', 'No phone')
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=400)

        # Buat order_id unik
        order_id = f"order-{uuid.uuid4().hex[:6]}-{int(time.time())}"

        # Simpan transaksi di database
        transaction = Transaction.objects.create(
            user=request.user,
            order_id=order_id,
            amount=amount,
            email=email,
            # fullname=fullname,
            status='pending',
            plan=plan,
        )

        # Konfigurasi Snap API
        snap = Snap(
            is_production=settings.MIDTRANS_IS_PRODUCTION,
            server_key=settings.MIDTRANS_SERVER_KEY,
            client_key=settings.MIDTRANS_CLIENT_KEY
        )

        # Definisikan parameter transaksi
        transaction_params = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": float(amount),
            },
            "customer_details": {
                # "first_name": fullname,
                "email": email,
                "phone": phone,
            },
            "callbacks": {
                "finish": "http://127.0.0.1:8000/payment-success/"  # Alamat localhost untuk testing
            }
        }

        try:
            # Generate Snap payment URL
            snap_response = snap.create_transaction(transaction_params)
            payment_url = snap_response['redirect_url']

            return JsonResponse({'payment_url': payment_url})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return render(request, 'subscribe.html')
    

import logging

logger = logging.getLogger(__name__)
@csrf_exempt
def payment_notification(request):
    core_api = CoreApi(
        is_production=settings.MIDTRANS_IS_PRODUCTION,
        server_key=settings.MIDTRANS_SERVER_KEY
    )
    try:
        # Parse notifikasi dari Midtrans
        logger.debug(f"Request body: {request.body.decode('utf-8')}")  # Log data mentah
        notification_data = json.loads(request.body)
        transaction_status = notification_data.get('transaction_status')
        order_id = notification_data.get('order_id')

        # Dapatkan transaksi berdasarkan order_id
        transaction = Transaction.objects.get(order_id=order_id)

        # Handle status transaksi
        if transaction_status == 'capture' or transaction_status == 'settlement':
            # Tandai transaksi sebagai berhasil
            transaction.status = 'settlement'
            transaction.save()

            # Buat atau perbarui langganan
            Subscription.objects.create(
                user=transaction.user,
                transaction=transaction,
                plan=transaction.plan,  # Ambil plan dari transaksi
                start_date=now(),
                end_date=now() + timedelta(days={
                    'basic': 30,
                    'premium': 60,
                    'enterprise': 90
                }.get(transaction.plan, 30)),  # Hitung durasi berdasarkan plan
                status='active'
            )
        elif transaction_status in ['deny', 'expire', 'cancel']:
            # Tandai transaksi sebagai gagal
            transaction.status = 'failed'
            transaction.save()
        
        # Kirim respons OK ke Midtrans
        return HttpResponse('OK', status=200)
    except Transaction.DoesNotExist:
        return HttpResponse(f"Transaction with order_id {order_id} not found.", status=404)
    except Exception as e:
        return HttpResponse(str(e), status=400)
    


def payment_success(request):
    return render(request, 'payment_success.html')

