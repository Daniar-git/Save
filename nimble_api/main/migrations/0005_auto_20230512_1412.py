# Generated by Django 3.1.6 on 2023-05-12 14:12

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230512_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=main.models.get_file_path, verbose_name='video'),
        ),
    ]
