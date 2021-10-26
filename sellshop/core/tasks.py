from django.db.models.aggregates import Count
from celery import shared_task
import time
from user.models import Subscribers
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from product.models import ProductVersion


@shared_task
def send_email_to_subscribers():
    subscribers_emails = Subscribers.objects.values_list('email', flat=True)
    # products = ProductVersion.objects.all()
    products = ProductVersion.objects.annotate(num_tags=Count('reviews')).order_by('-num_tags')[0:3]
    # products = ProductVersion.objects.filter('-created_at').annotate(num_tags=Count('reviews')).order_by('-num_tags')[0:3]
    for mail in subscribers_emails:
        body = render_to_string("subscribers_email.html", context= {
            'email': mail,
            'products': products,
        })
        msg = EmailMessage(subject='Subscriber mail', body=body, from_email=settings.EMAIL_HOST_USER,
                     to=[mail, ])
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)