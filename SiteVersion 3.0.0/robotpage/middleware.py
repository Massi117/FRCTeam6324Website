import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
    
LOGIN_URLS = [re.compile(settings.LOGOUT_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_NOT_EXEMPT_URLS'):
    LOGIN_URLS += [re.compile(url) for url in settings.LOGIN_NOT_EXEMPT_URLS]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        url_login = any(url.match(path) for url in LOGIN_URLS)

        if path == reverse('feed:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated() and url_is_exempt:
            return redirect(settings.LOGOUT_URL)
        elif not request.user.is_authenticated() and url_login:
            return  redirect(settings.NEED_LOGIN_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            return None
        else:
            return None   #redirect(settings.LOGIN_URL)
