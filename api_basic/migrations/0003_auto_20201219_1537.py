# Generated by Django 3.1.3 on 2020-12-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_auto_20201214_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/'),
        ),
    ]
