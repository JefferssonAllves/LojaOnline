from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('esqueceu_senha/', views.esqueceu_senha, name="esqueceu_senha"),

]