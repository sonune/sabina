# Generated by Django 3.2.8 on 2022-03-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0016_auto_20220318_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='15:12:27 not accurate', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='name',
            field=models.CharField(default='I love Neha and days_left is1888', max_length=499),
        ),
        migrations.AlterField(
            model_name='mera_jawwab',
            name='days_left',
            field=models.CharField(default=1888, max_length=233),
        ),
        migrations.AlterField(
            model_name='mera_jawwab',
            name='name',
            field=models.CharField(default='Mera Answers 1888', max_length=6000),
        ),
        migrations.AlterField(
            model_name='mera_sawwal',
            name='days_left',
            field=models.CharField(default=1888, max_length=233),
        ),
        migrations.AlterField(
            model_name='mera_sawwal',
            name='name',
            field=models.CharField(default='Sonu ka Sawwal 1888', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='days_left',
            field=models.CharField(default=1888, max_length=10),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='name',
            field=models.CharField(default='Neha ka answer 1888', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_question',
            name='name',
            field=models.CharField(default='Neha ka Question 1888', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uskamassage',
            name='sort',
            field=models.CharField(default=1888, max_length=10),
        ),
    ]
