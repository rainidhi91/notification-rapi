# Generated by Django 3.1.3 on 2021-01-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_notification_rapi', '0002_notification_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sent_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]