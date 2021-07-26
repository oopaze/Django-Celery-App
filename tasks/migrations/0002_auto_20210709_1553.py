# Generated by Django 3.1.2 on 2021-07-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='espera',
        ),
        migrations.AddField(
            model_name='task',
            name='tempo_espera',
            field=models.PositiveIntegerField(default=3, verbose_name='Tempo de espera'),
        ),
    ]
