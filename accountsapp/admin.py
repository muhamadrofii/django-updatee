from django.contrib import admin

# Register your models here.
from .models import CustomUser, ProfileParent, ProfileChild

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'Job')  # Tambahkan kolom

@admin.register(ProfileParent)
class ParentUser(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'pekerjaan', 'email', 'nomor_telepon', 'alamat', 'user_fullname')  # Kolom yang ditampilkan di admin
    search_fields = ('user__username', 'pekerjaan', 'email')  # Opsi pencarian
    list_filter = ('pekerjaan',)  # Filter berdasarkan pekerjaan

    def user_fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip()
    user_fullname.short_description = "Full Name"  # Nama kolom di admin

@admin.register(ProfileChild)
class ProfileChildAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'umur', 'pendidikan', 'bidang_minat', 'parent')  # Menampilkan kolom yang relevan
    search_fields = ('nama_lengkap', 'pendidikan')  # Mencari berdasarkan nama lengkap dan pendidikan
    list_filter = ('pendidikan', 'bidang_minat')  # Filter berdasarkan pendidikan dan bidang minat