from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'Log/index.html')
def login(request):
    loginResponse= User.objects.login_user(request.POST)
    if loginResponse['isLoggedIn']:
        request.session['user_id']= loginResponse['user'].id
        request.session['user_fname']=loginResponse['user'].name
        request.session['user_username']=loginResponse['user'].username
        return redirect(reverse('loginApp:loggedIn'))
    else:
        for error in loginResponse['errors']:
            messages.error(request,error)
        return redirect(reverse('loginApp:my_index'))

    return render(request, 'Log/index.html')
def registration(request):
    regResponse=User.objects.add_user(request.POST)
    if regResponse['isRegistered']:
        request.session['user_id']= regResponse['user'].id
        request.session['user_fname']=regResponse['user'].name
        request.session['user_username']=regResponse['user'].username
        return redirect(reverse('loginApp:success'))
    else:
        for error in regResponse['errors']:
            messages.error(request,error)
        return redirect(reverse('loginApp:my_index'))
def clear(request):
    return render(request, 'Log/index.html')
def success(request):

    return render(request, 'Log/yes.html')
def loggedIn(request):
    if not request.session:
        return redirect(reverse('loginApp:my_index'))
    return render(request, 'black/wishlist.html')
def logout(request):
    request.session.clear()
    return redirect(reverse('loginApp:my_index'))
