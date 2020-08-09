from django.urls import path
from operation import views

urlpatterns = [
    path('operation/',views.indexOperation,name='indexOperation'),
    path('operation/createReception',views.createReception,name='createReception'),
    path('operation/editReception/<int:pk>',views.editReception,name='editReception'),
    path('operation/editPreparation/<int:pk>',views.editPreparation,name='editPreparation'),
    path('operation/delete/<int:pk>',views.deleteOperation,name='deleteOperation'),
    path('operation/ExportateurData',views.ExportateurData,name='ExportateurData'),
    path('operation/ImportateurData',views.ImportateurData,name='ImportateurData'),
]
