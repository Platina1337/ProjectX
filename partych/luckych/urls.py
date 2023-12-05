from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegView.as_view(), name="registration"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name="logout"),
    path('add_note/', views.AddNoteView.as_view(), name='add_note'),
]