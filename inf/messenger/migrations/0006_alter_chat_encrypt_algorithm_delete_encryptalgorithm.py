# Generated by Django 5.1.6 on 2025-03-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_encryptalgorithm_alter_chat_encrypt_algorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='encrypt_algorithm',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='EncryptAlgorithm',
        ),
    ]
