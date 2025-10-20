from django.urls import path
from . import views

urlpatterns = [
    # 个人信息展示页面
    path('', views.personal_info_view, name='personal_info'),
]