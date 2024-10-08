from django.urls import path
from .views import referencia_create,referencia_delete,referencia_update,home

app_name = "porfolio"
urlpatterns = [
    path('home/',home,name='home'),
    path('referencia_create/',referencia_create,name="referencia_create"),
    path('referencia_update/<int:id>/',referencia_update,name='referencia_update'),
    path('referencia_delete/<int:id>/',referencia_delete,name='referencia_delete'),
    ]