# Generated by Django 4.1.2 on 2022-10-22 08:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_added_users_organizations_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('profile_image', models.URLField(default='https://ik.imagekit.io/ipy2x824p/eunoia/placeholders/profile-placeholder_pA2jdG52D.png', max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admins', to='organizations.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]