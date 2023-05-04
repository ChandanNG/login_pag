from django.urls import path,include
from . import views 
urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("index/",views.UserRegister,name="index"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
]
