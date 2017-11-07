from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from models import Google

class GoogleAdminSite(AdminSite):
    site_header = 'GnosisDB Administration'
    # template_name = 'DjangoGoogleAuthenticator/templates/admin/login.html'

admin = GoogleAdminSite(name='GoogleAdmin')

# admin.register(User)
# admin.register(Group)
admin.register(Google)
