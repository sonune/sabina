# Generated by Django 3.2.8 on 2022-03-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0014_auto_20220313_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('S_N', models.CharField(max_length=222)),
                ('update', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='14:54:21 not accurate', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='name',
            field=models.CharField(default='I love Neha and days_left is1890', max_length=499),
        ),
        migrations.AlterField(
            model_name='mera_jawwab',
            name='days_left',
            field=models.CharField(default=1890, max_length=233),
        ),
        migrations.AlterField(
            model_name='mera_jawwab',
            name='name',
            field=models.CharField(default='Mera Answers 1890', max_length=6000),
        ),
        migrations.AlterField(
            model_name='mera_sawwal',
            name='days_left',
            field=models.CharField(default=1890, max_length=233),
        ),
        migrations.AlterField(
            model_name='mera_sawwal',
            name='name',
            field=models.CharField(default='Sonu ka Sawwal 1890', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='days_left',
            field=models.CharField(default=1890, max_length=10),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='name',
            field=models.CharField(default='Neha ka answer 1890', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_question',
            name='name',
            field=models.CharField(default='Neha ka Question 1890', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uskamassage',
            name='sort',
            field=models.CharField(default=1890, max_length=10),
        ),
    ]