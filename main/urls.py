from django.urls import path
from . import views

urlpatterns = [
    path('words/<int:id>',views.home, name="words"),
    path('words/next', views.next, name= 'next'),
    path('words/prev', views.prev, name= 'prev'),
    path('words/random',views.rand, name = 'random')
]