import os

#package
from rest_framework.authtoken.models import Token
from templated_email import send_templated_mail

#django
from django.shortcuts import render, redirect
from django.urls import reverse
from utils.django_utils import check_reset_password_token

#models
from backend.models import User
# Create your views here.

def admin_send_reset_password_email(request):
    if request.method == 'GET':
        return render(request, 'admin/forgot_password.html')
    elif request.method == 'POST':
        email = request.POST.get("email", None)
        if email is not None:
            try:
                user = User.objects.get(email=email, is_staff=True)
            except Exception:
                return redirect('backend.admin_send_reset_password_email')

            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.delete()
                token = Token.objects.create(user=user)

            url = request.build_absolute_uri(reverse('backend.admin_reset_password') + '?token=' + token.key)
            send_templated_mail(
                    template_name='reset_password_admin',
                    from_email=os.environ.get('DEFAULT_FROM_EMAIL'),
                    recipient_list=[user.email],
                    context={
                        'username': user.username,
                        'email': user.email,
                        'url': url,
                },
            )
            return render(request, 'admin/forgot_password.html',
                        {
                            'status': 'sent_email'
                        }
            )
        else:
            return redirect('backend.admin_send_reset_password_email')

def admin_reset_password(request):
    if request.method == 'GET':
        token = request.GET.get("token", None)
        token_validate = check_reset_password_token(token)
        if token_validate['status'] == 'valid':
            request.session['token'] = token

        return render(request, 'admin/reset_password.html',
            {
                'status': token_validate['status']
            }
        )
    elif request.method == 'POST':
        token = request.session['token']
        password = request.POST.get('password', None)
        token_validate = check_reset_password_token(token)
        if token_validate['status'] == 'valid' and token_validate['user'] is not None and password:
            user = token_validate['user']
            user.set_password(password)
            user.save()
            token = Token.objects.get(user=user)
            token.delete()
            del request.session['token']
            status = 'password_changed'
        else:
            status = token_validate['status']

        return render(request, 'admin/reset_password.html',
            {
                'status': status
            }
        )









        