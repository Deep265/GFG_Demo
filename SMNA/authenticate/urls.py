from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("signup/",views.user_signup,name="singup"),
    path("login/",views.user_login,name="login"),
    path('logout/',views.user_logout,name='logout'),
]