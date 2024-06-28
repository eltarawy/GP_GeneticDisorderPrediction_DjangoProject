from django.urls import path
from . import views

urlpatterns = [
    path('prediction', views.prediction, name ='prediction'),    # /Gentic/prediction
    path('geno_prediction', views.geno_prediction, name ='geno_prediction'),    # /Gentic/geno_prediction

]