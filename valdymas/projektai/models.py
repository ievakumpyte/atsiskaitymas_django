from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse
# Create your models here.



class Klientas(models.Model):
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    imone = models.CharField("Įmonė", max_length=100)
    kontaktai = models.CharField("Kontaktai", max_length=100)

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'

    def __str__(self):
        return f'{self.vardas} {self.pavarde}'


class Darbuotojai(models.Model):
    prisijungimas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    pareigos = models.CharField("Pareigos", max_length=100)

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'

    def __str__(self):
        return f'{self.vardas} {self.pavarde}'


class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=100)
    pastabos = models.CharField("Pastabos", max_length=100, null=True, blank=True)


    BUSENOS_STATUS = (
        ('a', 'atlikta'),
        ('n', 'nepradeta'),
        ('p', 'pradeta'),

    )

    status = models.CharField("Busena", max_length=100, choices=BUSENOS_STATUS, null=True, blank=True)



    class Meta:
        verbose_name = 'Darbas'
        verbose_name_plural = 'Darbai'

    def __str__(self):
        return self.pavadinimas

class Saskaita(models.Model):
    israsymo_data = models.DateField("Data", null=True, blank=True)
    suma = models.FloatField("Suma", null=True, blank=True)
    projektas = models.ForeignKey("Projektas", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Sąskaita'
        verbose_name_plural = 'Sąskaitos'

    def __str__(self):
        return f'{self.israsymo_data}: {self.suma}'



class Projektas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=100)
    pradzios_data = models.DateField("Pradžios data", null=True, blank=True)
    pabaigos_data = models.DateField("Pabaigos data",null=True, blank=True)
    klientas = models.ForeignKey("Klientas",  on_delete=models.SET_NULL, null=True)
    vadovas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    darbuotojai = models.ManyToManyField(Darbuotojai,blank=True)
    darbai = models.ManyToManyField(Darbas,blank=True)

    cover = models.ImageField("Cover", upload_to='covers', null=True, blank=True)
    aprasymas = HTMLField(blank=True, null=True)



    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = 'Projektai'

    class Meta:
        ordering = ['pavadinimas']

    def __str__(self):
        return f'{self.pavadinimas} {self.pradzios_data} {self.pabaigos_data} {self.klientas}'

    def display_darbuotojai(self):
        return ', '.join((darbuotojai.vardas and darbuotojai.pavarde) for darbuotojai in self.darbuotojai.all())


    display_darbuotojai.short_description = 'Darbuotojai'