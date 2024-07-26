from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.template import loader
from django.utils.encoding import force_bytes
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

def password_reset_email(request, user, subject_template_name='registration/password_reset_subject.txt', email_template_name='registration/password_reset_email.html'):
    # Generate a token and uid for the email link
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    context = {
        'email': user.email,
        'domain': request.META['HTTP_HOST'],
        'site_name': 'Your Site',
        'uid': uid,
        'user': user,
        'token': token,
        'protocol': 'http',  # or 'https' if using HTTPS
    }

    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    # Render email content
    email = loader.render_to_string(email_template_name, context)

    # Send email using Django's email functionality
    send_mail(subject, email, 'vignesh@revaadigital.com', [user.email])

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    html_email_template_name = 'registration/password_reset_email.html' 
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
