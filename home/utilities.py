
from __future__ import print_function

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(form_data):
    
    from_email = settings.DEFAULT_EMAIL_FROM
   
    

    subject = form_data['subject']
    sender = form_data['email']
    reply_to = {
        "name": form_data['name'],
        "email": form_data['email'],}

    body = form_data['message']
    to = [{"email": 'luketedmusic@gmail.com', "name": 'Luke Edwards'}]

    params = {"parameter": "My param value", "subject": "New Subject"}
    msg = EmailMultiAlternatives(subject, body, sender, to=['luketedmusic@gmail.com'])
    try:
        msg.send()
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)