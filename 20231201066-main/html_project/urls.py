from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='html_project'),
    path('sections/<int:num>/', views.section, name='section'),
]