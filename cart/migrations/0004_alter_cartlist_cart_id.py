# Generated by Django 3.2.13 on 2022-06-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]