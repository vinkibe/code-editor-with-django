from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_editor, name='code_editor'),
    path('save/', views.save_code, name='save_code'), 
]