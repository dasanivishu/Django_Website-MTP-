from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.index, name='index'),
    path('Home/index.html',views.index,name='home'),                 
    path('Home/contact.html/',views.contact,name='contact'),
    path('Home/about.html/',views.about,name='about'),
    path('Home/pricing.html/',views.pricing,name='pricing'),
    path('Home/worksingle.html/',views.worksingle,name='worksingle'),
    path('Home/work.html/',views.work,name='work'),

]
