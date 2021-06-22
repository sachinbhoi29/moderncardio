from django.contrib import admin
from django.urls import path
from WebApp import views


urlpatterns = [
    path("",views.index, name='Home'),
    path("stories",views.stories, name='Stories'),
    path("information",views.information, name='information'),
    path("contact_us",views.contact_us, name='contact_us'),
    path("about_us",views.about_us, name='about_us'),
    path("appointment",views.appointment, name='appointment'),

]
