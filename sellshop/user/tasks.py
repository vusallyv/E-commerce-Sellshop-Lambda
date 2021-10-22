from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.db.models import Count
from celery import shared_task
from user.models import User
from product.models import Image, ProductVersion
from sellshop.settings import EMAIL_HOST_USER

from datetime import datetime

@shared_task
def send_mail_to_subscribers():
    allproductversions = ProductVersion.objects.annotate(
        num_rev=Count('review')).order_by('-num_rev')[:5]
    images = Image.objects.filter(is_main=True)
    users = User.objects.values_list('last_login', 'email', flat=True)
    for user in users:
        if (datetime.now().day - user.get('last_login').day) > 30:
            body = render_to_string('subscriber_mail.html', context={
                'email': user.get('email'),
                'allproductversions': allproductversions,
                'images': images,
            })
            msg = EmailMessage(subject='Subscriber mail', body=body,
                               from_email=EMAIL_HOST_USER,
                               to=[user.get('email'), ])
            msg.content_subtype = 'html'
            msg.send(fail_silently=True)
