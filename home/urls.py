from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='user_logout'),
]
