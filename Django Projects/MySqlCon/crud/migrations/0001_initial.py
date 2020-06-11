# Generated by Django 3.0.7 on 2020-06-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.CharField(max_length=20)),
                ('empName', models.CharField(max_length=100)),
                ('empEmail', models.EmailField(max_length=254)),
                ('empPhone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
