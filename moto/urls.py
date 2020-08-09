from django.urls import path
from moto import views

urlpatterns = [
    path('moto/',views.index,name='index'),
    path('moto/create',views.createMoto,name='createMoto'),
    path('moto/edit/<int:pk>',views.editMoto,name='editMoto'),
    path('moto/delete/<int:pk>',views.deleteMoto,name='deleteMoto'),

]
