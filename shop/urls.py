from django.urls import path, include
from . import views
urlpatterns = [
    path('search', views.searching, name='search'),
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.filtering, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_details, name='details'),



]
