from django.db import models



class ReservationsRestaurant(models.Model):
    nom = models.CharField(max_length=250)
    numeroTel = models.CharField(max_length=12, blank=True, null=True)
    mail = models.EmailField(max_length=200, blank=True, null=True)
    nombreDePersonnes = models.IntegerField(blank=True, null=True)
    tables = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom


class PlatDuJour(models.Model):
    plat = models.CharField(max_length=255)

    def __str__(self):
        return self.plat
