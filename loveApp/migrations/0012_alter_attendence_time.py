# Generated by Django 3.2.8 on 2022-03-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0011_auto_20220313_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='22:24:52 not accurate', max_length=50),
        ),
    ]
