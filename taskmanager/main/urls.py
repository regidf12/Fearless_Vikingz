from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name="about"),
    path('roadmap', views.roadmap, name="roadmap"),
    path('team', views.team, name="team"),
    path('faq', views.faq, name="faq")
]
