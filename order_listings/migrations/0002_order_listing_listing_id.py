# Generated by Django 4.1.2 on 2022-11-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_listing',
            name='listing_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
