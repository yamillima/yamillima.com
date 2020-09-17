# Generated by Django 2.2.16 on 2020-09-17 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_lead_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
