from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Choice
from .models import YouTubeVideo

# Mendaftarkan model YouTubeVideo ke halaman admin
@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_id', 'uploaded_at', 'image', 'category')  # Menampilkan kolom title, youtube_id, dan tanggal upload di daftar
    search_fields = ('title', 'youtube_id')  # Memungkinkan pencarian berdasarkan title dan youtube_id
    list_filter = ('uploaded_at',)  # Menambahkan filter berdasarkan tanggal upload


# Konfigurasi Inline untuk Choice
# @admin.register(YouTubeVideo)
class ChoiceInline(admin.TabularInline):  # Gunakan TabularInline untuk tampilan tabel
    model = Choice
    extra = 4  # Jumlah pilihan kosong yang ditampilkan di admin

# Konfigurasi Model Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'order')  # Kolom yang ditampilkan di daftar pertanyaan
    list_filter = ('quiz',)  # Filter berdasarkan kuis
    search_fields = ('text',)  # Pencarian berdasarkan teks pertanyaan
    inlines = [ChoiceInline]  # Tambahkan pilihan secara inline

# Konfigurasi Model Quiz
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'id')  # Kolom yang ditampilkan di daftar kuis
    search_fields = ('title',)  # Pencarian berdasarkan judul

# Daftarkan Model di Admin
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)