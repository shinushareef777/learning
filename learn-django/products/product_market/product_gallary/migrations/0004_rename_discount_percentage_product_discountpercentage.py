# Generated by Django 4.2.1 on 2023-05-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_gallary', '0003_product_discount_percentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_percentage',
            new_name='discountPercentage',
        ),
    ]
