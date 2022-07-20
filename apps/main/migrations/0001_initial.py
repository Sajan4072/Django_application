# Generated by Django 4.0.5 on 2022-07-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('time', models.TimeField(primary_key=True, serialize=False)),
                ('service_charge', models.FloatField(max_length=100)),
                ('surge_charge', models.FloatField(max_length=100)),
                ('initial_fare', models.FloatField(max_length=100)),
                ('kilometer_charge', models.FloatField(max_length=100)),
            ],
            options={
                'verbose_name': 'Fare',
                'verbose_name_plural': 'Fares',
                'db_table': 'fare',
            },
        ),
    ]
