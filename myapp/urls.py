from django.urls import path
from myapp import views

urlpatterns = [
    path('myapp/',views.index,name='index'),
    path('flower/<int:id>/', views.detail,name='detail'),
    path('flower/create',views.create,name='create'),
    path('flower/edit/<int:pk>',views.edit,name='edit'),
    path('flower/delete/<int:pk>',views.delete, name='delete'),
]
