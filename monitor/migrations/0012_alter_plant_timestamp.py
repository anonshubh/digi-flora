# Generated by Django 3.2 on 2021-04-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_alter_device_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
