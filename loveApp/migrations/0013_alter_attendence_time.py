# Generated by Django 3.2.8 on 2022-03-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0012_alter_attendence_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='22:30:06 not accurate', max_length=50),
        ),
    ]