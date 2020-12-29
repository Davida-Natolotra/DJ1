from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('main/',views.main),
    path('main/topbar',views.topbar,name='topbar'),
    
]
