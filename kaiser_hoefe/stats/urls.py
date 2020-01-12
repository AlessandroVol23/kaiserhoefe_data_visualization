from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='index'),
    path('women_count', views.get_women_count, name='women_count')
]