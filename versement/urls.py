from django.urls import path
from versement import views

urlpatterns = [
    path('versement/',views.indexVersement,name='indexVersement'),
    path('versement/create',views.createVersement,name='createVersement'),
    path('versement/edit/<int:pk>',views.editVersement,name='editVersement'),
    path('versement/delete/<int:pk>',views.deleteVersement,name='deleteVersement'),

]
