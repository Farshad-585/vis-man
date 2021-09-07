# Generated by Django 3.2.6 on 2021-09-07 05:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('accomodation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='AU', unique=True)),
                ('role', models.CharField(max_length=100)),
                ('nightstay', models.BooleanField(default=False)),
                ('checkin', models.DateTimeField(default='2021-09-07 05:55:57', editable=False)),
                ('planned_checkout', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, editable=False, null=True)),
                ('emergency_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('emergency_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('emergency_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='AU', unique=True)),
                ('emergency_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('site', models.ManyToManyField(to='survey.Site')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('checkin', models.DateTimeField(editable=False)),
                ('checkout', models.DateTimeField(editable=False)),
                ('nightstay', models.BooleanField(editable=False)),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.visitor')),
            ],
        ),
    ]
