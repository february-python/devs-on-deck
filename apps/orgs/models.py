from django.db import models

# Create your models here.
class OrgManager(models.Manager):
    pass


class Org(models.Model):
    org_name        =   models.CharField(255)
    first_name      =   models.CharField(255)
    last_name       =   models.CharField(255)
    contact_email   =   models.CharField(255)
    org_address     =   models.CharField(255)
    org_city        =   models.CharField(255)
    org_stage       =   models.CharField(255)
    password        =   models.CharField(500)
    created_at      =   models.DateTimeField(auto_now_add)
    updated_at      =   models.DateTimeField(auto_now)

    objects         =   OrgManager