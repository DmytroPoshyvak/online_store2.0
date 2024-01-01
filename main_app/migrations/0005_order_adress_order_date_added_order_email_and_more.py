# Generated by Django 4.1.3 on 2023-06-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_photos_photot'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='time_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='product_total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='time_edited',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='product_total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productinfavourite',
            name='time_edited',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photot',
            field=models.ImageField(upload_to='mediac'),
        ),
    ]