# Generated by Django 4.1.2 on 2022-11-01 06:54

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('donor_org_name', models.CharField(max_length=200)),
                ('donor_org_id', models.CharField(max_length=200)),
                ('charity_org_name', models.CharField(max_length=200)),
                ('charity_ord_id', models.CharField(max_length=200)),
                ('collection_date', models.DateField()),
                ('collection_timeslot', models.CharField(choices=[('12am - 2am', '_12AM'), ('2am - 4am', '_2AM'), ('4am - 6am', '_4AM'), ('6am - 8am', '_6AM'), ('8am - 10am', '_8AM'), ('10am - 12pm', '_10AM'), ('12pm - 2pm', '_12PM'), ('2pm - 4pm', '_2PM'), ('4pm - 6pm', '_4PM'), ('6pm - 8pm', '_6PM'), ('8pm - 10pm', '_8PM'), ('10pm - 12am', '_10PM')], max_length=254, verbose_name='timeslot option')),
                ('collection_address_contact_name', models.CharField(max_length=50)),
                ('collection_address_contact_number', models.CharField(max_length=50)),
                ('collection_address_details', models.CharField(max_length=200)),
                ('collection_address_postal_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('delivery_address_contact_name', models.CharField(max_length=50)),
                ('delivery_address_contact_number', models.CharField(max_length=50)),
                ('delivery_address_details', models.CharField(max_length=200)),
                ('delivery_address_postal_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('completion_time', models.DateTimeField(null=True)),
                ('need_delivery', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('completed', 'COMPLETED'), ('cancelled', 'CANCELLED')], default='open', max_length=254, verbose_name='order status')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
