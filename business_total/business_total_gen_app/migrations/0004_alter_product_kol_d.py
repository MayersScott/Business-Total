# Generated by Django 4.2.7 on 2023-11-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_total_gen_app', '0003_product_kol_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kol_d',
            field=models.CharField(default=1, max_length=255),
        ),
    ]
