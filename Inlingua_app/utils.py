# utils.py
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_welcome_email(to_email, name):
    subject = "Welcome to Inlingua"
    body = render_to_string('email/welcome_email.html', {'name': name})
    email = EmailMessage(
        subject,
        body,
        'vignesh@revaadigital.com',
        [to_email],
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.send()
