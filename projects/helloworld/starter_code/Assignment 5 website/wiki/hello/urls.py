from django.urls import path
from . import views

urlpatterns = {
    path("index", views.index), 
    path("entry/<str:name>", views.getpage)
}