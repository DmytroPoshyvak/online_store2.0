# Generated by Django 4.1.3 on 2023-10-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_order_prodcut_in_basket_productinbasket_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
