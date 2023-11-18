from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth.models import User


def review_mail_sender(name, email, review):
    subject = f"{name} review"
    context = {
        'name': name,
        'email': email,
        'review': review
    }
    message = render_to_string('review_email_message.txt', context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list=[email], fail_silently=False)


def daily_10am_mail_sender():
    emails = User.objects.values_list('email', flat=True).all()
    subject = "صبح بخیر"
    message = render_to_string('daily_email_message.txt')
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list=emails, fail_silently=False)
