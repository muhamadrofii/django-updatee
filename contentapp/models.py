from django.db import models

# Create your models here.
class YouTubeVideo(models.Model):
    CATEGORY_CHOICES = [
        ('Post Test', 'Post Test'),
        ('Parenting Dasar', 'Parenting Dasar'),
        ('Ide Bekal Sekolah', 'Ide Bekal Sekolah'),
        ('Ruang Baca', 'Ruang Baca'),
        ('Animal', 'Animal'),
        ('ABC & 123', 'ABC & 123'),
        ('Warna & Bentuk', 'Warna & Bentuk'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=255, blank=True, null=True)  # Judul Video
    description = models.TextField(blank=True, null=True)  # Deskripsi Video
    youtube_id = models.CharField(max_length=255, blank=True, null=True)  # ID Video YouTube (misal: '8lGeIh4oYJ8')
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Tanggal Upload
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, blank=True, null=True)  # Kategori Video
    image = models.ImageField(upload_to='thumbnails/', null=True, blank=True)  # Gambar Thumbnail Video

    def __str__(self):
        return self.title if self.title else f"Video ID: {self.youtube_id}"
    

class Quiz(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField secara eksplisit untuk primary key
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.text[:50]}"

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text