# Generated by Django 4.1.3 on 2023-07-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_productinbasket_session_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.product'),
        ),
    ]
