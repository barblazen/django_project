# Generated by Django 4.2.5 on 2025-02-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
        migrations.AddField(
            model_name="book",
            name="review",
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
