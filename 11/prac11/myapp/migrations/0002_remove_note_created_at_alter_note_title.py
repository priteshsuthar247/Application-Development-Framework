# Generated by Django 5.2 on 2025-04-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="note",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
