# Generated by Django 4.2.9 on 2024-04-01 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_alter_sale_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(default=datetime.date(2024, 4, 1)),
        ),
    ]