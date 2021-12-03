from django.urls import path
from .views import *

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('sign/',SignUpPage.as_view(),name='signin'),
    path('login/',LoginView.as_view(),name='login'),
    
]

