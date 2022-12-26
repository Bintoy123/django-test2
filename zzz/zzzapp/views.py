from django.shortcuts import render
from zzzapp.form import UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'zzzapp/index.html')
    
@login_required
def special(request):
    return render(request,'zzzapp/special.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def base(request):
    return render(request,'zzzapp/base.html')

def other(request):
    return render(request,'zzzapp/other.html')

def form(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_prof = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_prof.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            prof = user_prof.save(commit=False)
            prof.butter = user

            if 'profile' in request.FILES:
                prof.profile = request.FILES['profile']
            if 'resume' in request.FILES:
                prof.resume = request.FILES['resume']

            prof.save()
            registered = True
        else:
            return HttpResponse('Invalid login')
    else:
        user_form = UserForm()
        user_prof = UserProfileForm()
    return render(request,'zzzapp/form.html',{'user_form':user_form,
                                              'user_prof':user_prof,
                                              'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            return HttpResponse('Invalid Login')
    return render(request,'zzzapp/login.html')
