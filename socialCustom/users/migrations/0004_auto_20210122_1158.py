# Generated by Django 3.1.5 on 2021-01-22 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser1_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser1',
            name='email',
        ),
        migrations.AddField(
            model_name='newuser1',
            name='email_address',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, unique=True, verbose_name='email_address address'),
            preserve_default=False,
        ),
    ]
