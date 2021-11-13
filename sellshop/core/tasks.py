from django.db.models.aggregates import Count
from celery import shared_task
import time
from user.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from product.models import ProductVersion
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_email_to_subscribers():
    present_time = timezone.now()
    end_date = present_time - timedelta(days=7)
    subscribers_emails = Subscriber.objects.values_list('email', flat=True)
    products = ProductVersion.objects.filter(created_at__gte=end_date).annotate(num_tags=Count('product_reviews')).order_by('-num_tags')[0:3]
    for mail in subscribers_emails:
        body = render_to_string("subscribers_email.html", context= {
            'email': mail,
            'products': products,
        })
        msg = EmailMessage(subject='Subscriber mail', body=body, from_email=settings.EMAIL_HOST_USER,
                     to=[mail, ])
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)