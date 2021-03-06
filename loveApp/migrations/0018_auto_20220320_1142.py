# Generated by Django 3.2.8 on 2022-03-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveApp', '0017_auto_20220318_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='I_am_there_sonu',
            new_name='I_am_there_lucky',
        ),
        migrations.RenameField(
            model_name='uska_answer',
            old_name='Neha_ka_Jawab_of_specifice_question',
            new_name='Sabina_ka_Jawab_of_specifice_question',
        ),
        migrations.RemoveField(
            model_name='mera_jawwab',
            name='days_left',
        ),
        migrations.RemoveField(
            model_name='mera_sawwal',
            name='days_left',
        ),
        migrations.AlterField(
            model_name='attendence',
            name='Time',
            field=models.CharField(default='00:00:00 not accurate', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='name',
            field=models.CharField(default='I love Sabina and days_left is2022-03-20', max_length=499),
        ),
        migrations.AlterField(
            model_name='mera_jawwab',
            name='name',
            field=models.CharField(default='Mera Answers 2022-03-20', max_length=6000),
        ),
        migrations.AlterField(
            model_name='mera_sawwal',
            name='name',
            field=models.CharField(default='lucky ka Sawwal 2022-03-20', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='days_left',
            field=models.CharField(default=1886, max_length=10),
        ),
        migrations.AlterField(
            model_name='uska_answer',
            name='name',
            field=models.CharField(default='Sabina ka answer 2022-03-20', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uska_question',
            name='name',
            field=models.CharField(default='Sabina ka Question 2022-03-20', max_length=6000),
        ),
        migrations.AlterField(
            model_name='uskamassage',
            name='sort',
            field=models.CharField(default=1886, max_length=10),
        ),
    ]
