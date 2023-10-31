# Generated by Django 4.2.5 on 2023-10-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="potData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ultra", models.FloatField(max_length=15)),
                ("gyro_x", models.FloatField(max_length=15)),
                ("gyro_y", models.FloatField(max_length=15)),
                ("gyro_z", models.FloatField(max_length=15)),
                ("gps_time", models.CharField(max_length=15)),
                ("gps_lat", models.FloatField(max_length=15)),
                ("gps_long", models.FloatField(max_length=15)),
            ],
        ),
    ]
