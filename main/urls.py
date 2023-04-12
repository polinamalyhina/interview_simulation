from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('get_question/', views.get_question, name='get_question'),
]
