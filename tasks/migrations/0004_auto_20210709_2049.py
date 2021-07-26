# Generated by Django 3.1.2 on 2021-07-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('registrada', 'Registrada'), ('em_espera', 'Em Espera'), ('em_execucao', 'Em Execução'), ('finalizada', 'Finalizada')], default='registrada', max_length=20),
        ),
    ]