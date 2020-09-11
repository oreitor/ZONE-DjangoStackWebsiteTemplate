from django.urls import path
from . import views

# http://127.0.0.1:8000

urlpatterns = [
    path('datascience', views.ds, name='datascience'),
    path('artificialintelligence', views.ai, name='artificialintelligence'),
    path('machinelearning', views.ml, name='machinelearning'),
    path('deeplearning', views.dl, name='deeplearning'),
]