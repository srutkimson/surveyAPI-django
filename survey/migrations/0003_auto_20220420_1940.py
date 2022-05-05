# Generated by Django 3.2.12 on 2022-04-20 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20220420_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='mChoice',
        ),
        migrations.AddField(
            model_name='answer',
            name='mChoices',
            field=models.ManyToManyField(related_name='mChoices', to='survey.Choice'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 19, 37, 10, 445873)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 19, 37, 10, 445862), editable=False),
        ),
    ]