# Generated by Django 5.1.3 on 2024-12-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
