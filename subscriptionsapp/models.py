from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from accountsapp.models import ProfileParent  # Ganti 'app_profile' dengan nama aplikasi ProfileParent Anda


class Transaction(models.Model):
    PLAN_CHOICES = [
        ('trial', 'Trial Plan'),
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
        ('ultimate', 'Ultimate Plan'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('settlement', 'Settlement'),
        ('failed', 'Failed'),
    ]

    # Hubungan ke model User (opsional jika sudah ada ProfileParent)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Hubungan ke ProfileParent
    # profile = models.ForeignKey(ProfileParent, on_delete=models.CASCADE, null=True, blank=True)

    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Tambahan informasi dari ProfileParent jika diperlukan
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.order_id} - {self.get_plan_display()}"

    def default_end_date(self):
        """Mengembalikan end_date yang sesuai dengan jenis langganan."""
        plan_duration = {
            'trial': 7,          # 7 hari untuk Trial Plan
            'monthly': 30,       # 30 hari untuk 1-Month Plan
            'semi_annual': 180,  # 180 hari untuk 6-Month Plan
            'annual': 365,       # 365 hari untuk 12-Month Plan
        }
        duration = plan_duration.get(self.plan, 30)  # Default ke 30 hari jika plan tidak ditemukan
        return now() + timedelta(days=duration)

def default_end_date(subscription):
    """Mengembalikan end_date yang sesuai dengan jenis langganan."""
    plan_duration = {
        'basic': 30,     # 30 hari untuk Basic Plan
        'premium': 60,   # 60 hari untuk Premium Plan
        'enterprise': 90 # 90 hari untuk Enterprise Plan
    }
    
    # Ambil durasi berdasarkan plan, default ke 30 jika plan tidak dikenal
    duration = plan_duration.get(subscription.plan, 30)
    
    return now() + timedelta(days=duration)

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
        ('enterprise', 'Enterprise Plan'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.OneToOneField('Transaction', on_delete=models.CASCADE, null=True, blank=True)
    # plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    plan = models.CharField(max_length=20)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField()  # Tidak ada default, dihitung secara dinamis
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Override save untuk menghitung end_date berdasarkan plan."""
        if not self.end_date:
            self.end_date = default_end_date(self)  # Menghitung end_date berdasarkan plan
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username} - {self.plan} - {self.status}"
    
    def is_active(self):
        """Mengembalikan True jika langganan aktif dan belum kedaluwarsa."""
        return self.status == 'active' and now() < self.end_date