from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="İndex"), #path(route, view, opt(kısayol ismi))
]