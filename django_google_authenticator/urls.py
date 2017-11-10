from django.conf.urls import url, include
from views import login_view
from admin import admin

urlpatterns = [
    url(r'^admin/login/$', login_view),
    url(r'^admin/', include(admin.site.urls)),
]
