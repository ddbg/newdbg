from django.contrib import admin
from django.urls import path
from .views import *



#app_name='common'

urlpatterns = [
        
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name= "logout"),
    path('signUp/', signUp, name="signUp"),
]