from django.urls import path
from . import views

urlpatterns = [


    path('',views.registration,name = 'registration'),
    path('registration1/', views.registration1, name='registration1'),
]