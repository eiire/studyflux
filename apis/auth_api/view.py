# @method_decorator(ensure_csrf_cookie)
import json
import random
import string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from general_page.models import Confirm


def signup(request):
    user_json = json.loads(request.POST.get('user'))
    # check all data from json user

    confirm_code = request.POST.get('confirm_code')
    account_activation_token = request.COOKIES.get('account_activation_token')

    if account_activation_token is None or confirm_code is None:
        email_exist = False

        for _user in User.objects.all():
            if _user.is_active and _user.email == user_json['email']:
                email_exist = True

        if not email_exist:
            User.objects.filter(email=user_json['email'], is_active=False).delete()
            User.objects.filter(username=user_json['username'], is_active=False).delete()

            try:
                user = User.objects.create_user(username=user_json['username'], email=user_json['email'], password=user_json['password'], is_active=False)
            except IntegrityError:
                return JsonResponse({
                    'error': True,
                    'description': 'The user with this username is already registered'
                })

            confirm_code = str(random.randint(1000, 9999))  # test
            account_activation_token = ''.join(random.choice(string.ascii_lowercase) for i in range(100))

            Confirm.objects.create(code=confirm_code, user=user, token=account_activation_token).save()

            send_mail('Activate Your Account', confirm_code, "bulax.d@mail.ru",
                      [user.email], fail_silently=False)

            response = JsonResponse({
                'error': False,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active
                }
            })

            response.set_cookie(key='account_activation_token', value=account_activation_token)

            return response
        else:
            return JsonResponse({
                'error': True,
                'description': 'The user with this mail is already registered'
            })

    elif account_activation_token and confirm_code:
        try:
            confirm = Confirm.objects.get(code=confirm_code, token=account_activation_token)
        except:
            return JsonResponse({'error': True, 'description': 'Incorrect code'})

        if confirm:
            user = User.objects.get(username=confirm.user.username)
            user.is_active = True
            user.save()
            # print(user)
            user = authenticate(username=user_json['username'], password=user_json['password'])
            login(request, user)

            send_mail('Your Account is Activated', 'Thx', "bulax.d@mail.ru",
                      [user.email], fail_silently=False)

            return JsonResponse({
                'error': False,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active
                }
            })
        else:
            return JsonResponse({'error': True})


def signin(request):
    user_json = json.loads(request.POST.get('user'))
    username = user_json['login']
    password = user_json['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)

            return JsonResponse({
                'error': False,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active
                }
            })
        else:
            return JsonResponse({
                'error': True,
                'description': 'The user email not confirm'
            })
    else:
        return JsonResponse({
            'error': True,
            'description': 'Incorrect password or login'
        })


def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'error': False,
            'user': {
                'username': request.user.username,
                'email': request.user.email,
                'is_active': request.user.is_active
            }
        })
    else:
        return JsonResponse({
            'error': True,
            'description': 'Anonymous'
        })


def _logout(request):
    logout(request)

    return JsonResponse({'error': False})


# user.save()
# if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         return redirect('home')
# else:
#     form = UserCreationForm()

# render_to_string('account_activation_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'uid': user.pk,
        #     'token': 'dfffffffff',
        # })

# confirm_link = 'https://' + request.META['HTTP_HOST'] + '/signup/?account_activation_token=' + ''.join(random.choice(string.ascii_lowercase) for i in range(100))
        # print(confirm_link)
