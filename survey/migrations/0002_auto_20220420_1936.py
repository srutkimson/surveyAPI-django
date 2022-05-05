# Generated by Django 3.2.12 on 2022-04-20 16:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 19, 36, 35, 620792)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 19, 36, 35, 620781), editable=False),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='mChoice',
            field=models.ManyToManyField(related_name='mChoices', to='survey.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='sChoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sChoice', to='survey.choice'),
        ),
    ]