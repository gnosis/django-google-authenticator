from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
import pyotp


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_view(request, authentication_form=AuthenticationForm,
    current_app=None, extra_context=None):

    form = None
    context = {}
    redirect_to = '/admin/'

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        provided_gauth_code = request.POST.get('2fa')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'google'):
                # User has google auth enabled
                # Check Google Auth
                totp = pyotp.TOTP(user.google.gauth_key)
                user_gauth_code = totp.now()
                if user_gauth_code == provided_gauth_code:
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    form.errors.update({'gauth_code': [u'This field is required']})
            elif user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_to)
            else:
                form.errors.update({'gauth_code': [u'This field is required']})
        else:
            # gauth_code doesn't get validated this we force to raise an error
            form.errors.update({'gauth_code': [u'This field is required']})
    else:
        form = authentication_form(request)


    context = {
        'form': form,
        'redirect_field_name': redirect_to,
    }

    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, 'django_google_authenticator/admin/login.html', context)
