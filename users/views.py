from django.shortcuts import render

# Create your views here.
class UserLoginView(LoginView):
    template_name = "login.html"
   