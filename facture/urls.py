from django.urls import path
from facture import views
urlpatterns = [
    path('facture/edit/<int:id>',views.editFacture,name='editFacture'),
    path('facture/preview/<int:id>',views.previewFacture,name='previewFacture'),
    path('facture/initFacture',views.initFacture,name='initFacture'),
    path('facture/editFactureMoto/<int:id>',views.editFactureMoto,name='editFactureMoto'),
    path('facture/editBLMoto/<int:id>',views.editBLMoto,name='editBLMoto'),
    path('facture/previewFactureMoto/<int:id>',views.previewFactureMoto,name='previewFactureMoto'),
    path('facture/previewBLMoto/<int:id>',views.previewBLMoto,name='previewBLMoto'),
]
