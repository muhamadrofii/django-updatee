# Generated by Django 5.1.3 on 2024-12-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0004_alter_quiz_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideo',
            name='category',
            field=models.CharField(blank=True, choices=[('Post Test', 'Post Test'), ('Parenting Dasar', 'Parenting Dasar'), ('Ide Bekal Sekolah', 'Ide Bekal Sekolah'), ('Ruang Baca', 'Ruang Baca'), ('Animal', 'Animal'), ('ABC & 123', 'ABC & 123'), ('Warna & Bentuk', 'Warna & Bentuk'), ('Science', 'Science')], max_length=255, null=True),
        ),
    ]