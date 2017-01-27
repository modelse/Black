from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Items
from ..Log.models import User

def index(request):
    return render(request, 'Log/index.html')
def wishlist(request):
    context = {
    'Items': Items.objects.all(),
    'Users': User.objects.all()
    }
    return render(request, 'black/wishlist.html', context)
def display(request,id):
    context = {
    'Items': Items.objects.filter(id=id),
    'id':id
    }
    return render(request, 'black/display.html', context)
def home(request):
    return redirect(reverse('blackApp:wishlist'))
def add(request):
    print request.session['user_id']
    return render(request, 'black/add.html')
def addItem(request):
    errors=Items.objects.validate(request)
    # print errors
    if not errors ==[]:
        for error in errors:
            messages.info(request, error)
        return redirect(reverse('blackApp:add'))
    else:
        createdItem=Items.objects.createItem(request)

        return redirect(reverse('blackApp:wishlist'))
        print createdItem
def delete(request, id):

    context = {
    'Items': Items.objects.filter(id=id).delete(),
    'id':id
    }
    return redirect('/wishlist', context)

def remove(request):
    return redirect(reverse('blackApp:wishlist'))
