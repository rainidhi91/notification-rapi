# Generated by Django 3.1.3 on 2021-01-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_notification_rapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
