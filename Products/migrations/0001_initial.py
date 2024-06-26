# Generated by Django 4.2.9 on 2024-03-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('product_feature', models.CharField(max_length=50)),
                ('product_cost', models.CharField(max_length=50)),
                ('product_img', models.FileField(default=None, max_length=250, null=True, upload_to='products/')),
            ],
        ),
    ]
