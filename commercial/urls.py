from django.urls import path
from commercial import views

urlpatterns = [
    path('commercial/homemotocom',views.indexcom,name='homemotocom'),
    path('commercial/createMotoCom',views.createMotoCom,name='createMotoCom'),
    path('commercial/editmotocom/<int:pk>',views.editMotoCom,name='editMotoCom'),
    path('commercial/editFactMotoCom/<int:id>',
         views.editFactureMotoCom, name='editFactMotoCom'),
    path('commercial/previewFactureMotoCom/<int:id>',views.previewFactureMotoCom, name='previewFactureMotoCom'),
    path('commercial/editBLMotoCom/<int:id>',views.editBLMotoCom, name='editBLMotoCom'),
    path('commercial/previewBLMotoCom/<int:id>',
         views.previewBLMotoCom, name='previewBLMotoCom'),

]
