# Generated by Django 3.1.5 on 2021-04-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_auto_20210402_0526"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
