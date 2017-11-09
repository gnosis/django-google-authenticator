from django.db import models
from django.contrib.auth.models import User

class Google(models.Model):
    """
    This models adds the Google Authenticator info to the standard
    User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gauth_key = models.CharField(max_length=16) # a 16 chars key
