# Generated by Django 5.0.2 on 2024-03-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims_app', '0003_remove_claim_id_alter_claim_claim_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
