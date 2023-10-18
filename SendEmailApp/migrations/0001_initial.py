# Generated by Django 4.2 on 2023-10-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('imp_date', models.DateField()),
                ('event_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('template', models.CharField(max_length=200)),
            ],
        ),
    ]