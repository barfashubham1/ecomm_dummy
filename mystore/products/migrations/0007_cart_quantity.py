# Generated by Django 3.1.5 on 2021-04-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_auto_20210405_1019"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(default=int),
            preserve_default=False,
        ),
    ]
