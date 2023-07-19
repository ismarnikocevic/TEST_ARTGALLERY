from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
from. import views
from PROJEKAT import views
from django.views.generic.base import TemplateView # new




urlpatterns = [
    
    path('', views.index),
    path('dom/', views.dom),
    path('biography/', views.biography), 
    path('gallery/', views.gallery), 
    path('album/', views.album), 
    path('photo1/', views.photo1), 
    path('slika2/', views.slika2),
    path('photo2/', views.photo2),
    path('photo3/', views.photo3),
    path('photo4/', views.photo4),
    path('photo5/', views.photo5),
    path('photo6/', views.photo6),
    path('photo7/', views.photo7),
    path('photo8/', views.photo8),
    path('photo9/', views.photo9),
    path('photo10/', views.photo10),
    path('photo11/', views.photo11),
    path('photo12/', views.photo12),
    path('photo13/', views.photo13),
    path('photo14/', views.photo14),
    path('photo15/', views.photo15),
    path('photo16/', views.photo16),
    path('photo17/', views.photo17),
    path('photo18/', views.photo18),
    path('photo19/', views.photo19),
  
   
    path('primjer/', views.primjer),

   



   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)