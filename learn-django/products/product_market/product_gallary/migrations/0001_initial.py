# Generated by Django 4.2.1 on 2023-05-25 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('thumbnail', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product_gallary.product')),
            ],
        ),
    ]