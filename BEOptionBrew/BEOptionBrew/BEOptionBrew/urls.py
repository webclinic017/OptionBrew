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
from .views import ( MarketViews, UserViews)

urlpatterns = [
    path('admin/', admin.site.urls),

    # REGISTER / LOGIN 
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/me/', get_current_user, name='current-user'),

    # USER DATA 
    # path('dashboard/balance', )

    # TRANSACTIONS 
    path('addfunds/', UserTransactions.as_view(), name='add-funds'),

    # TRADES 
    path('open-position/', open_position_view, name='open-position'),
    
    # MARKET DATA
    path('market-data/<str:ticker>/live/', live_data_view, name='live-data-ticker'),
    path('market-data/<str:ticker>/live-data/', get_live_data, name='get-live-data'),
    path('market-data/<str:ticker>/historical/<str:time_span>/', historical_data_view, name='historical-data-ticker'),
]
