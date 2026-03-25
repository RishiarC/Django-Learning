from django.urls import path
from . import views #from current directory import views


#jb koi main url pe aayega to ye sab dikhayega ye sub url patterns hai jo arogya app ke liye hai
# aur yha se view par jayega jo ki sab chai products ko dikhayega
urlpatterns = [

    path("", views.all_chai, name="all_chai"),
    
]