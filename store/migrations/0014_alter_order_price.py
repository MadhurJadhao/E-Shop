# Generated by Django 4.1.2 on 2022-11-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
