from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Mailing, Subscriber

@shared_task
def send_mailing(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        html_content = render_to_string('mailer/email_template.html', {
            'subscriber': subscriber,
            'mailing': mailing,
        })
        msg = EmailMultiAlternatives(mailing.subject, '', 'kakoi-to-address@gmail.com', [subscriber.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    mailing.is_sent = True
    mailing.save()