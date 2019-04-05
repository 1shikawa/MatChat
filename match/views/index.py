from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from forms.login import LoginForm

def top(request):
    return render(request, 'index.html')


class Login(LoginView):
    '''ログインページ'''
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LogoutView, LoginRequiredMixin):
    '''ログアウトページ'''
    template_name = 'index.html'
