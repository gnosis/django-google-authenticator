from django.conf.urls import url, include
from .admin import admin
from .views import login_view

urlpatterns = [
    url(r'^admin/login/$', login_view),
    url(r'^admin/', include(admin.site.urls)),
]
