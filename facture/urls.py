from django.urls import path
from facture import views

urlpatterns = [
    path('facture/edit/<int:id>',views.editFacture,name='editFacture'),
    path('facture/preview/<int:id>',views.previewFacture,name='previewFacture'),
    path('facture/initFacture',views.initFacture,name='initFacture')
]
