# Generated by Django 5.0.7 on 2024-07-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("soil", "0003_alter_upload_soil_data_class_n"),
    ]

    operations = [
        migrations.AlterField(
            model_name="upload_soil_data_class",
            name="N",
            field=models.FloatField(),
        ),
    ]
