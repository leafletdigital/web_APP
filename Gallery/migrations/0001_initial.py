# Generated by Django 4.2.9 on 2024-03-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.FileField(default=None, max_length=250, null=True, upload_to='gallery/')),
            ],
        ),
    ]
