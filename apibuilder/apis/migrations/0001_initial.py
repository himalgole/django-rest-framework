# Generated by Django 4.2.7 on 2023-11-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('level', models.CharField(choices=[('1', 'Primary'), ('2', 'Lower Secondary'), ('3', 'Secondary'), ('4', '+2'), ('5', 'Bachelors'), ('6', 'Masters'), ('7', 'PHD')], max_length=20)),
            ],
        ),
    ]
