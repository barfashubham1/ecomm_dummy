# Generated by Django 3.1.5 on 2021-04-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0014_auto_20210408_0904"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
