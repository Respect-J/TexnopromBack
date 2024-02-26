# Generated by Django 5.0.1 on 2024-02-25 11:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('mainimg', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('password', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
