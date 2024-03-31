# Generated by Django 5.0.3 on 2024-03-28 00:12

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.IntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_desc', models.CharField(max_length=200, null=True)),
                ('product_photo', models.ImageField(null=True, upload_to='images/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('sale_date', models.DateField(default=datetime.date(2024, 3, 27))),
                ('digital_signature', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='DealerJob',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_desc', models.CharField(max_length=200, null=True)),
                ('job_date', models.DateField(null=True)),
                ('job_photo', models.ImageField(null=True, upload_to='images/')),
                ('job_status', models.IntegerField(default=1)),
                ('job_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_app.sale')),
            ],
        ),
    ]
