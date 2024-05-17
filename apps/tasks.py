from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_to_email(to_email: str):
    send_mail('Tema', 'xabar', FROM_EMAIl, [to_email])
    return {'message': f'Email sent {to_email}'}
