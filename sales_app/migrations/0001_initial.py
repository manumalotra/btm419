# Generated by Django 4.2.9 on 2024-03-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('customer_email', models.CharField(max_length=200)),
                ('customer_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.IntegerField()),
                ('sale_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('digital_signature', models.CharField(max_length=200)),
            ],
        ),
    ]