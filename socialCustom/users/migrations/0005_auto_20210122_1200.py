# Generated by Django 3.1.5 on 2021-01-22 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210122_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser1',
            name='email_address',
        ),
        migrations.AddField(
            model_name='newuser1',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
