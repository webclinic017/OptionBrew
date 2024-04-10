"""
URL configuration for BEOptionBrew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import UserListCreate, UserDetail, ContactInformationListCreate, ContactInformationDetail, UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('contact-info/', ContactInformationListCreate.as_view(), name='contact-info-list'),
    path('contact-info/<int:pk>/', ContactInformationDetail.as_view(), name='contact-info-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
