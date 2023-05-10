
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.getToDo, name="yapilacaklar_listesi"),
    path('create', views.createToDoList, name="ekle_todolist"),
]
