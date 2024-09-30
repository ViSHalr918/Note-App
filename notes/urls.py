
from django.urls import path
from notes import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path("register/",views.UsercreationView.as_view()),

    path("token/",ObtainAuthToken.as_view())
    
]