# Generated by Django 3.2.6 on 2023-07-03 07:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('members', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sender_id', models.TextField(max_length=255)),
                ('receiver_id', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessageGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sender_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatgroup')),
            ],
        ),
    ]
