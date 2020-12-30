from django.urls import path
from accounts import views
urlpatterns = [
    path('login/',views.loginPage,name='loginPage'),
    path('logout/',views.logoutUser,name='logout'),
    path('account/',views.accounts,name='account')
]
