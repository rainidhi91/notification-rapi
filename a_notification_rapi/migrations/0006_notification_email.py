# Generated by Django 3.1.3 on 2021-02-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_notification_rapi', '0005_auto_20210106_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
