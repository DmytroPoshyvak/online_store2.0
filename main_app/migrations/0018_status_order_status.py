# Generated by Django 4.1.3 on 2023-12-13 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=225)),
                ('is_active', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.status'),
        ),
    ]
