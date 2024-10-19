"""
URL configuration for BloodBank project.

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
from app.views import DonorAdminAPIView, BloodInventoryAPIView,UserRegistrationView,BloodRequestAdminAPIView,BloodInventoryAdminAPIView,BloodRequestAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)


urlpatterns = [
        # path('admin/', admin.site.urls),  # Admin URL

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('admin/donors/', DonorAdminAPIView.as_view(), name='all-donors'),
    path('admin/request/<int:id>/', BloodRequestAdminAPIView.as_view(), name='blood-request-admin'),
    path('admin/donors/<int:id>/', DonorAdminAPIView.as_view(), name='single-donor'), 
    path('admin/inventory/<int:id>', BloodInventoryAPIView.as_view(), name='inventory-id'),  
    path('admin/inventory', BloodInventoryAPIView.as_view(), name='inventory')  ,

    path('allinventory', BloodInventoryAPIView.as_view(), name='all-inventory'),  
    path('request/<int:id>', BloodRequestAPIView.as_view(), name='delete-request'),  
    path('request', BloodRequestAPIView.as_view(), name='add-request'),  
    path('register', UserRegistrationView.as_view(), name='user-registration'),
  
]

