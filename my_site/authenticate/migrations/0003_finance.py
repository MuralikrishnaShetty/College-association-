# Generated by Django 3.2.10 on 2022-10-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_auto_20221029_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('event', models.CharField(max_length=20)),
                ('cost', models.BigIntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
            ],
        ),
    ]
