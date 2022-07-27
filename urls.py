from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('signup/', views.signup, name="User Sign Up"),
    path('signin/', views.signin, name="User Sign In"),
    path('signout/', views.signout, name="User Sign Out"),
    
    path('dashboard/', views.dashboard, name="Dashboard"),
    
]
