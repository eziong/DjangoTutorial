# Generated by Django 3.1.5 on 2021-01-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210122_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser1',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]