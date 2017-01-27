from __future__ import unicode_literals
import re, bcrypt
from django.db import models
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')



class UserManager(models.Manager):
    def add_user(self, postData):
        errors=[]
        if len(postData['name'])<2:
            errors.append('Name needs more characters.')
        elif not name.match(postData['name']):
            errors.append('No numbers allowed in first name')
        if len(postData['username'])<2:
            errors.append('Username needs more characters.')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Not a valid email address.')
        if len(postData['password'])<8:
            errors.append('Password needs to be 9 characters or more!')
        if postData['password']!=postData['confirm']:
            errors.append('Password does not match!')
        if len(postData['hired_date'])<2:
            errors.append('Please enter a date')

        modelsResponse={}

        if errors:
            modelsResponse['isRegistered'] = False
            modelsResponse ['errors'] = errors
        else:
            modelsResponse['isRegistered'] = True
            hashed_password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user=self.create(name= postData['name'], email=postData['email'], username=postData['username'], hired_date=postData['hired_date'], password=hashed_password)
            modelsResponse['isRegistered'] = True
            modelsResponse['user']= user

        return modelsResponse

    def login_user(self,postData):
        errors=[]
        modelsResponse= {}
        user = self.filter(username = postData['username2'])
        if not user:
            errors.append('Invalid username!')
        else:

            if bcrypt.checkpw(postData['password2'].encode(), user[0].password.encode()):
                modelsResponse['isLoggedIn']= True
                modelsResponse['user']= user[0]
            else:
                errors.append('Invalid username/password combination.')
        if errors:
            modelsResponse['isLoggedIn'] = False
            modelsReponse['errors'] = errors

        return modelsResponse


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=250)
    hired_date=models.DateField('%m/%d/%Y')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()
