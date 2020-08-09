from django.urls import path
from caisseTana import views

urlpatterns = [
    path('caisseTana/',views.indexTana,name='indexTana'),
    path('caisseTana/refSolde/<int:pk>',views.refSoldeTana,name='refSoldeTana'),
    path('caisseTana/create',views.createCaisseTana,name='createCaisseTana'),
    path('caisseTana/edit/<int:pk>',views.editCaisseTana,name='editCaisseTana'),
    path('caisseTana/delete/<int:pk>',views.deleteCaisseTana,name='deleteCaisseTana'),

]
