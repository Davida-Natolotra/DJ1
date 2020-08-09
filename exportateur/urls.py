from django.urls import path
from exportateur import views

urlpatterns = [
    path('exportateur/',views.indexExportateur,name='indexExportateur'),
    path('exportateur/create',views.createExportateur,name='createExportateur'),
    path('exportateur/edit/<int:pk>',views.editExportateur,name='editExportateur'),
    path('exportateur/delete/<int:pk>',views.deleteExportateur,name='deleteExportateur')

]
