# Generated by Django 3.2.8 on 2022-03-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0009_auto_20220313_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uska_question',
            name='date',
        ),
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='20:07:48 not accurate', max_length=50),
        ),
    ]
