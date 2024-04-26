# Generated by Django 5.0.3 on 2024-04-18 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Adhaar_no', models.BigIntegerField()),
                ('Pan_no', models.BigIntegerField()),
                ('Qualification', models.CharField(max_length=250)),
                ('User_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
