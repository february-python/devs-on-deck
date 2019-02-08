from django.db import models

# Create your models here.
class OrgManager:
    pass


class Org(models.Model):
    org_name    =   CharField(255)
    first_name  =   CharField(255)
    last_name   =   CharField(255)
    email       =   CharField(255)
    address     =   CharField(255)
    city        =   CharField(255)
    state       =   CharField(2)
    password    =   CharField(500)
    created_at  =   DateTimeField(auto_now_add)
    updated_at  =   DateTimeField(auto_now)

    objects     =   UserManager