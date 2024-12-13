from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

# Create your views here.
def index(request):
    return render(request, 'index.html')

def berita(request):
    return render(request, 'berita.html')

def tentangKami(request):
    return render(request, 'tentangKami.html')

def faq(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        
        # Simpan data ke database
        Feedback.objects.create(nama=nama, email=email, feedback=feedback)
        
        # Tampilkan notifikasi sukses
        messages.success(request, 'Feedback Anda berhasil dikirim. Terima kasih!')
        return redirect('faq')  # Tetap di halaman FAQ
    
    return render(request, 'faq.html')