from django.db import models
import bcrypt
import re
from apps.devs.models import Dev
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class OrgManager(models.Manager):
    def validate(self, form_data):
        errors= []
        if len(form_data['org_name']) < 2:
            errors.append('Organization name must be more than 2 characters')
        if len(form_data['fname']) < 2:
            errors.append('First name must be more than 2 characters')
        if len(form_data['lname']) < 2:
            errors.append('Last name must be more than 2 characters')
        if not EMAIL_REGEX.match(form_data['cemail']):
            errors.append('Email address is in wrong format')
        if len(form_data['oadd']) < 2:
            errors.append('The organization address must be more than 4 characters')
        if len(form_data['ocity']) < 2:
            errors.append('The organization city must be more than 4 characters')
        user_list = self.filter(contact_email=form_data['cemail'])
        if len(user_list) > 0:
            errors.append("Email already in use.")
        if len(form_data['pwd']) < 8:
            errors.append("Password is too short.")
        return errors
    
    def login_validate(self, form_data):
        if not EMAIL_REGEX.match(form['cemail']):
            errors.append('Email address is in wrong format')
        if len(form_data['pwd']) < 8:
            errors.append("Password is too short.")
        return errors
        

    def create_user(self, form_data):
        pw_hash =bcrypt.hashpw(form_data['pwd'].encode(), bcrypt.gensalt())
        return self.create(
            org_name        = form_data['org_name'],
            first_name      = form_data['fname'],
            last_name       = form_data['lname'],
            contact_email   = form_data['cemail'],
            org_address     = form_data['oadd'],
            org_city        = form_data['ocity'],
            org_state       = form_data['ostate'],
            password        = pw_hash,  
        )
        
class Org(models.Model):
    org_name        =   models.CharField(max_length=255)
    first_name      =   models.CharField(max_length=255)
    last_name       =   models.CharField(max_length=255)
    contact_email   =   models.CharField(max_length=255)
    org_address     =   models.CharField(max_length=255)
    org_city        =   models.CharField(max_length=255)
    org_state       =   models.CharField(max_length=2)
    password        =   models.CharField(max_length=500)
    created_at      =   models.DateTimeField(auto_now_add = True)
    updated_at      =   models.DateTimeField(auto_now = True)

    objects         =   OrgManager()

class Position(models.Model):
    pos_name        =   models.CharField(max_length=255)
    description     =   models.TextField()
    pos_org         =   models.ManyToManyField(Org, related_name="pos_org")
    pos_dev         =   models.ManyToManyField(Dev, related_name="pos_dev")

class Skill(models.Model):
    skill_name      =   models.CharField(max_length=255)
    position        =   models.ManyToManyField(Position, related_name="pos")
    developer       =   models.ManyToManyField(Dev, related_name="dev")
