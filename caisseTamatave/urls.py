from django.urls import path
from caisseTamatave import views

urlpatterns = [
    path('caisseTamatave/',views.indexTamatave,name='indexTamatave'),
    path('caisseTamatave/refSolde/<int:pk>',views.refSoldeTamatave,name='refSoldeTamatave'),
    path('caisseTamatave/create',views.createCaisseTamatave,name='createCaisseTamatave'),
    path('caisseTamatave/edit/<int:pk>',views.editCaisseTamatave,name='editCaisseTamatave'),
    path('caisseTamatave/delete/<int:pk>',views.deleteCaisseTamatave,name='deleteCaisseTamatave'),

]
