# Generated by Django 3.2.8 on 2022-03-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0005_auto_20220312_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='name',
            field=models.CharField(default='Neha1896', max_length=499),
        ),
    ]