# Generated by Django 5.1.6 on 2025-03-05 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_message_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsakey',
            name='output_n',
        ),
        migrations.RemoveField(
            model_name='rsakey',
            name='output_public_key',
        ),
        migrations.CreateModel(
            name='RSAOutputKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.TextField()),
                ('public_key', models.TextField()),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rsa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
