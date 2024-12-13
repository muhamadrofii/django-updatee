from django.contrib import admin

# Register your models here.
from .models import Feedback
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'feedback')  # Tambahkan kolom lain jika ada
    list_filter = ('email',)  # Menambahkan filter berdasarkan email
    # ordering = ('-id',)  # Mengurutkan data (contoh: berdasarkan ID secara descending)