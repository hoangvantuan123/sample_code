# Generated by Django 4.2.1 on 2023-05-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Users",
        ),
    ]