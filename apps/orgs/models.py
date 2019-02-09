from django.db import models

# Create your models here.
class OrgManager(models.Manager):
    pass


class Org(models.Model):
    org_name        =   models.CharField(max_length=255)
    first_name      =   models.CharField(max_length=255)
    last_name       =   models.CharField(max_length=255)
    contact_email   =   models.CharField(max_length=255)
    org_address     =   models.CharField(max_length=255)
    org_city        =   models.CharField(max_length=255)
    org_state       =   models.CharField(max_length=255)
    password        =   models.CharField(max_length=500)
    created_at      =   models.DateTimeField(auto_now_add=True)
    updated_at      =   models.DateTimeField(auto_now=True)

    objects         =   OrgManager()