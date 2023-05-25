from django.shortcuts import render,redirect
from allauth.account import views
from django.urls import reverse_lazy

# Create your views here.
class LoginView(views.LoginView):
    template_name="accounts/login.html"


class LogoutView(views.LogoutView):
    template_name="accounts/logout.html"

    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        
        return redirect("/")
    

class SignupView(views.SignupView):

    template_name="accounts/signup.html"
    success_url=reverse_lazy("index")
