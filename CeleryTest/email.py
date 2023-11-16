from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_review_mail(name, email, review):
    subject = f"{name} review"
    context = {
        'name': name,
        'email': email,
        'review': review
    }
    message = render_to_string('email_message.txt', context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list=[email], fail_silently=False)
