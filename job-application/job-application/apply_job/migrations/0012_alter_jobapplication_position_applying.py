# Generated by Django 4.1.2 on 2022-10-19 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apply_job", "0011_alter_jobapplication_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="position_applying",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="apply_job.position",
            ),
        ),
    ]
