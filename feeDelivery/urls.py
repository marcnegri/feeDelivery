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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserView.user_list),
    path('users/<int:pk>/', UserView.user_detail),
    path('menus/', MenuView.menu_list),
    path('menus/<int:pk>/meals/', MenuDetailsView.menu_details_meals),
    path('meals/', MealView.meal_list),
    path('mealcategories/', MealCategoryView.meal_category_list, name='get_all_meal_category'),
    path('companies/', CompanyView.company_list),

]
