from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.produtos, name='produtos'),
    path('teste/', view=views.teste, name='teste'),

]