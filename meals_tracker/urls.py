"""
URL configuration for meals_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from Food_Diary import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp.as_view()),
    path('user/', views.UserView.as_view()),
    path('food/', views.FoodListView.as_view()),
    path('food/<int:id>/',views.FoodUpdateDeleteView.as_view()),
    path('food-diary/', views.FoodListView.as_view()),
    path('weight/',views.WeightListView.as_view()),
    
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', views.LogoutView.as_view()),

]
