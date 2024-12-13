from django.db import models
# myapp/models.py
from django.contrib.auth.models import AbstractUser, User
# # from django.db import models

class CustomUser(AbstractUser):
    Job = models.CharField(max_length=225, blank=True, null=True)  # Field baru
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups',  # Ganti nama reverse accessor
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',  # Ganti nama reverse accessor
        blank=True
    )


class ProfileParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Hubungan dengan model User
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    pekerjaan = models.CharField(max_length=100, blank=True, null=True)  # Pekerjaan
    email = models.EmailField(blank=True, null=True)                      # Email
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)  # Nomor Telepon
    alamat = models.TextField(blank=True, null=True)                      # Alamat
    #childrenname = models.

    def __str__(self):
        # return f"{self.user.username}'s Profile"

            # Menggabungkan username, first_name, dan last_name dari model User
        fullname = f"{self.user.first_name} {self.user.last_name}".strip()
        return f"{fullname} ({self.user.username})'s Profile"


class ProfileChild(models.Model):
    parent = models.ForeignKey(ProfileParent, on_delete=models.CASCADE, related_name='children')  # Relasi ke ProfileParent
    nama_lengkap = models.CharField(max_length=200)  # Nama Lengkap Anak
    umur = models.PositiveIntegerField()  # Umur
    PILIHAN_PENDIDIKAN = [
        ('belum sekolah', 'Belum Sekolah'),
        ('tk_a', 'TK A'),
        ('tk_b', 'TK B'),
        ('sd_1', 'SD Kelas 1'),
        ('sd_2', 'SD Kelas 2'),
        ('sd_3', 'SD Kelas 3'),
        ('sd_4', 'SD Kelas 4'),
        ('sd_5', 'SD Kelas 5'),
        ('sd_6', 'SD Kelas 6'),
    ]
    pendidikan = models.CharField(max_length=20, choices=PILIHAN_PENDIDIKAN)  # Pilihan Pendidikan
    BIDANG_MINAT = [
        ('olahraga', 'Olahraga'),
        ('berhitung', 'Berhitung'),
    ]
    bidang_minat = models.CharField(max_length=200, choices=BIDANG_MINAT, blank=True, null=True)  # Bidang Minat

    def __str__(self):
        return f"Anak: {self.nama_lengkap} ({self.umur} tahun)"

