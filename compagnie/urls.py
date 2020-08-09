from django.urls import path
from compagnie import views

urlpatterns = [
    path('compagnie/',views.indexCompagnie,name='indexCompagnie'),
    path('compagnie/create',views.createCompagnie,name='createCompagnie'),
    path('compagnie/edit/<int:pk>',views.editCompagnie,name='editCompagnie'),
    path('compagnie/delete/<int:pk>',views.deleteCompagnie,name='deleteCompagnie')
]
