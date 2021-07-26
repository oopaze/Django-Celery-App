from tasks.models import Task
from time import sleep

from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task
from django.shortcuts import get_object_or_404


@shared_task
def execute_task(id):
    task = get_object_or_404(Task, id=id)
    
    task.status = "em_execucao"
    task.save()

    message = f"A Task {task.titulo} foi executada em {task.tempo_espera} segundos.\n"
    message += f"Descrição: {task.descricao}."

    sleep(task.tempo_espera)

    task.status = "finalizada"
    task.save()

    send_mail(
        f'Task - {task.titulo}',
        message,
        settings.DEFAULT_FROM_EMAIL,
        ['pedroosd28@gmail.com'],
        fail_silently=False,
    )

    return "ok"
