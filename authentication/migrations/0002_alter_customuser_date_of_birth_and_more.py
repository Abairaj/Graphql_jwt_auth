# Generated by Django 4.2.5 on 2023-09-19 04:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female")],
                max_length=150,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_id",
            field=models.UUIDField(
                default=uuid.UUID("cee3784c-83ea-4bea-9d8d-9e67312d3983")
            ),
        ),
    ]
