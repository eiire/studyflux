from django.contrib.auth.models import User
from django.http import JsonResponse


def get_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
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
            'description': 'User not authenticate'
        })
