"""
Definition of urls for ChanFAD.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('channels/', views.ChannelListView.as_view(), name = 'channels'),
    path('channel/<slug:pk>', views.ChannelDetailView.as_view(), name = 'channel-entry'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
