from . import views
from django.urls import path

urlpatterns=[
    path("home/", view=views.home,name="home"),
    path("singleTicket/<int:id>",view=views.single_Ticket,name="single_Ticket"),
    path("Name/<str:customer_name>",view=views.ticketByName,name="ticketByName"),
]