from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', views.enter_cow_id_view, name='enter_cow_id'),
    path('milk/<str:cow_id>/', views.milk_cow_view, name='milk_cow'),
    path('cow/', views.cow_details_view, name='cow_details'),
    path('reset_bsod/', views.reset_bsod_view, name='reset_bsod'),
    path('list_cows/', views.list_cows_view, name='list_cows'),
    path('milk_report/', views.milk_report_view, name='milk_report'),
    path('reset_bsod/', views.reset_bsod_view, name='reset_bsod'),
    path('reset_all_milk/', views.reset_all_milk_view, name='reset_all_milk'),
]
