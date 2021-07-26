# Generated by Django 3.1.2 on 2021-07-09 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('espera', models.TimeField(default=datetime.time(0, 0, 3), verbose_name='Tempo de espera')),
            ],
        ),
    ]