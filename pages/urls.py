from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name ='about'),    # /pages/home
    path('diseases', views.diseases, name ='diseases'),
    path('contact', views.contact, name ='contact'),
    path('Cancer', views.Cancer, name ='Cancer'),
    path('Alzheimer', views.Alzheimer, name ='Alzheimer'),
    path('CysticFibrosis', views.CysticFibrosis, name ='CysticFibrosis'),
    path('Diabetes', views.Diabetes, name ='Diabetes'),
    path('Hemochromatosis', views.Hemochromatosis, name ='Hemochromatosis'),
    path('LeberHereditaryOpticNeuropathy', views.LeberHereditaryOpticNeuropathy, name ='LeberHereditaryOpticNeuropathy'),
    path('LeighSyndrome', views.LeighSyndrome, name ='LeighSyndrome'),
    path('MitochondrialMyopathy', views.MitochondrialMyopathy, name ='MitochondrialMyopathy'),
    path('TaySachs', views.TaySachs, name ='TaySachs'),


]