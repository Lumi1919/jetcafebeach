from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = 'home'

urlpatterns = [
    path('', views.index, name="accueil"),
    path('reservations_list/', views.reservations_list, name="reservations_list"),
    path('bar_restaurant/', views.bar_restaurant, name="bar_restaurant"),
    path('menu_jour/', views.menu_jour, name="menu_jour"),
    path('evenement/', views.evenement, name="evenement"),
    path('brunch/', views.brunch, name="brunch"),
    path('ceremonie/', views.ceremonie, name="ceremonie"),
    path("confirmation/", views.confirmation_reservation,  name="confirmation_reservation")
]
