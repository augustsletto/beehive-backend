# Generated by Django 5.0.3 on 2024-03-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(default='../default_profile_tvknyo', upload_to='images/'),
        ),
    ]
