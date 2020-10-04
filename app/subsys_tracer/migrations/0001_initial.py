# Generated by Django 3.1.1 on 2020-10-04 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('encryption_keys', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=12)),
                ('phone2', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('date', models.PositiveIntegerField(max_length=8)),
                ('time', models.PositiveIntegerField(max_length=2)),
                ('location', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('encryption_keys', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StayHomeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=32)),
                ('images', models.CharField(max_length=32)),
                ('videos', models.CharField(max_length=32)),
                ('documents', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tracer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('encryption_keys', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('age', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('address', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=32)),
                ('test_result', models.CharField(choices=[('True', 'Positive'), ('False', 'Negative'), ('None', 'Unknown')], max_length=5)),
                ('encryption_keys', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
