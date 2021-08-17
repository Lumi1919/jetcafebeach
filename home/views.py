from django.shortcuts import render, redirect
from .models import ReservationsRestaurant
from .formulaires import ReservationsRestaurantForm
from .models import PlatDuJour
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/connexion')
def reservations_list(request):
    return render(request, 'reservation_list.html', {'dataReservationsRestaurant': ReservationsRestaurant.objects.all()})


def menu_jour(request):
    platDuJour = PlatDuJour.objects.get()
    model = ReservationsRestaurant
    form_class = ReservationsRestaurantForm
    if request.method == "POST":
        form = ReservationsRestaurantForm(request.POST).save()
        return redirect('/confirmation')

    else:
        form = ReservationsRestaurantForm()

    return render(request, 'menu_jour.html', {'form': form, 'dataReservationsHotel': ReservationsRestaurant.objects.all(), 'platDuJour': platDuJour})


def bar_restaurant(request):
    return render(request, 'bar_restaurant.html')


def confirmation_reservation(request):
    return render(request, 'confirmation_reservation.html')


def evenement(request):
    return render(request, 'evenement.html')


def brunch(request):
    model = ReservationsRestaurant
    form_class = ReservationsRestaurantForm
    if request.method == "POST":
        form = ReservationsRestaurantForm(request.POST).save()
        return redirect('/confirmation')

    else:
        form = ReservationsRestaurantForm()
    return render(request, 'brunch.html', {'form': form, 'dataReservationsHotel': ReservationsRestaurant.objects.all()})


def ceremonie(request):
    return render(request, 'ceremonie.html')


def contact(request):
    return render(request, 'contact.html')


