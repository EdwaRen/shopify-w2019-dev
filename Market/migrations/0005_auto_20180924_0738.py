# Generated by Django 2.1.1 on 2018-09-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0004_auto_20180924_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='value',
        ),
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
    ]
