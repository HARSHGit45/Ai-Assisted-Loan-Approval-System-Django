# Generated by Django 5.0.7 on 2024-07-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_application_passport_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='ml_prediction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]