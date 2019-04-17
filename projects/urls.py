from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='projects'),
    path('<int:pk>', views.detail, name='project_detail'),
]