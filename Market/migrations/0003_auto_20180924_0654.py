# Generated by Django 2.1.1 on 2018-09-24 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0002_auto_20180924_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lineitem_order_created', to='Market.Product'),
        ),
    ]
