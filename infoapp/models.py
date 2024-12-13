from django.db import models

# Create your models here.
class Feedback(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.nama