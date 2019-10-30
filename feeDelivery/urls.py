"""feeDelivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import UserView, MenuView, CompanyView, MenuDetailsView
from webapp.views import MealView, MealCategoryView
from webapp.views.CompanyView import CompanyList
from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserView.user_list),
    path('users/<int:pk>/', UserView.user_detail),
    url(r'^users/(?P<_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', UserView.user_detail_by_email),
    path('menus/', MenuView.menu_list),
    path('menus/<int:pk>/meals/', MenuDetailsView.menu_details_meals),
    path('meals/', MealView.meal_list),
    path('mealcategories/', MealCategoryView.meal_category_list, name='get_all_meal_category'),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyView.company_details),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
