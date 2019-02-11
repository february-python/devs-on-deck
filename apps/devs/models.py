from django.db import models
import re
import bcrypt

# Create your models here.
class DevManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(form_data['first_name']) < 2:
            errors.append("First name must be at least 3 characters.")
        elif not form_data['first_name'].isalpha():
            errors.append("First name must contain only letters.")
        if len(form_data['last_name']) < 2:
            errors.append("Last name must be at least 3 characters.")
        elif not form_data['last_name'].isalpha():
            errors.append("Last name must contain only letters.")
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Email is invalid.")
        if form_data['address'] < 1:
            errors.append("Address cannot be empty.")
        if form_data['city'] < 1:
            errors.append("City cannot be empty.")
        if len(form_data['password']) < 8:
            errors.append("Password must be at least 8 characters.")
        if form_data['confirm_pw'] != form_data['password']:
            errors.append("Passwords must match.")

        existing_devs = self.filter(email=form_data['email'])
        if existing_devs:
            errors.append('Email already in use.')
        return errors

    def create_dev(self, form_data):
        pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            street = form_data['street'],
            city=form_data['street'],
            state=form_data['state'],
            email=form_data['email'],
            pw_hash=pw_hash
        )

    def validate_login(self, form_data):
        errors = []
        
        try:
            dev = Dev.objects.get(email=form_data['email'])
        except:
            errors.append('Unable to log you in. Please register or try again.')
            return errors
        if dev:
            if not bcrypt.checkpw(form_data['password'].encode(), dev.pw_hash.encode()):
                errors.append('Unable to log you in. Please register or try again.')
                return errors


class Dev(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DevManager()