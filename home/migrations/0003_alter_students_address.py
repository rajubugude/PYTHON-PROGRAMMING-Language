# Generated by Django 4.2 on 2023-04-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
