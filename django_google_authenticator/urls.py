from django.conf.urls import url

from .admin import admin
from .views import login_view

app_name = 'django_google_authenticator'

urlpatterns = [
    url(r'^admin/login/$', login_view),
    url(r'^admin/', admin.site.urls),
]
