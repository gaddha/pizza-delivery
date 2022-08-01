from django.urls import path
from .views import helloauthview
from . import views



urlpatterns = [
  path('',helloauthview.as_view(),name='helloauth'),
  path('signup/',views.UserCreationView.as_view(),name='sign_up'),
  ]