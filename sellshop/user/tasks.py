from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.db.models import Count
from celery import shared_task
from user.models import User
from product.models import Image, ProductVersion
from sellshop.settings import EMAIL_HOST_USER
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_mail_to_users():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=30)
    allproductversions = ProductVersion.objects.annotate(
        num_rev=Count('product_reviews')).order_by('-num_rev')[:5]
    images = Image.objects.filter(is_main=True)
    users = User.objects.all()
    for user in users:
        if user.last_login < enddate:
            body = render_to_string('subscriber_mail.html', context={
                'email': user.email,
                'allproductversions': allproductversions,
                'images': images,
            })
            msg = EmailMessage(subject='Subscriber mail', body=body,
                               from_email=EMAIL_HOST_USER,
                               to=[user.email, ])
            msg.content_subtype = 'html'
            msg.send(fail_silently=True)
