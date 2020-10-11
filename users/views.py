from django import forms
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.http import HttpResponse
from users.forms import *
from users.models import *



# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserRegisterForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save(commit=False)
            user.is_active = False
            user.position_id = 0
            user.save()
            sign_up_form = UserRegisterForm()
            messages.success(
                request, 'Registration is done. Please check your email!', extra_tags='alert')
        
        return render(request, 'users/sign_up.html', {'sign_up_form': sign_up_form})
    else:
        sign_up_form = UserRegisterForm()
    return render(request, 'users/sign_up.html', {'sign_up_form': sign_up_form})



class CustomLogin(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        user = auth.get_user(self.request)

        self.request.session['email'] = str(user.email)
        self.request.session['user_id'] = int(user.id)
        messages.success(
                self.request, 'Registration is done. Please check your email!', extra_tags='alert')
        
        return render(self.request, 'users/login.html')

        


