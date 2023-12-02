# Generated by Django 4.1.13 on 2023-12-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clubbing", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="date_posted",
        ),
        migrations.RemoveField(
            model_name="review",
            name="text",
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
        migrations.AlterField(
            model_name="review",
            name="club",
            field=models.CharField(max_length=255),
        ),
    ]
