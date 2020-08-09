from django.urls import path
from importateur import views

urlpatterns = [
    path('importateur/',views.indexImportateur,name='indexImportateur'),
    path('importateur/create',views.createImportateur,name='createImportateur'),
    path('importateur/edit/<int:pk>',views.editImportateur,name='editImportateur'),
    path('importateur/delete/<int:pk>',views.deleteImportateur,name='deleteImportateur'),

]
