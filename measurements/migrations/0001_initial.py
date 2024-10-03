# Generated by Django 5.1.1 on 2024-09-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_plate', models.CharField(max_length=255)),
                ('date_time_a', models.DateTimeField(blank=True, null=True)),
                ('date_time_b', models.DateTimeField(blank=True, null=True)),
                ('avg_speed', models.FloatField(null=True)),
                ('make', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
