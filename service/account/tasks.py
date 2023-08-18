from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_about_registration(user_id):
    user = User.objects.get(id=user_id)
    subject = f'Hi! {user.first_name}'
    message = "Thank you for registration"
    sender = settings.EMAIL_HOST_USER
    send_mail(
        subject,
        message,
        sender,
        [user.email]
    )
