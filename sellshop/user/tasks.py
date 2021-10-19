from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from celery import shared_task
from user.models import Subscriber
from sellshop.settings import EMAIL_HOST_USER


@shared_task
def send_mail_to_subscribers():
    subscriber_emails = Subscriber.objects.values_list('email', flat=True)
    for mail in subscriber_emails:
        body = render_to_string('subscriber_mail.html', context={
            'email': mail
        })
        msg = EmailMessage(subject='Subscriber mail', body=body,
                           from_email=EMAIL_HOST_USER,
                           to=[mail, ])
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)
