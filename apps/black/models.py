from __future__ import unicode_literals
from django.db import models
from ..Log.models import User

# Create your models here.

class ItemsManager(models.Manager):
    def validate(self, request):
        errors=[]
        if len(request.POST['addItem'])<4:
            errors.append('Please name an item. Must be at least 3 characters long.')
        return errors


    def createItem(self, request):

        Items.objects.create(item_name=request.POST['addItem'], user=User.objects.get(id=request.session['user_id']))






class Items(models.Model):
    item_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="people")
    objects = ItemsManager()
