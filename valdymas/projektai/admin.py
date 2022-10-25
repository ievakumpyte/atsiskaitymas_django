from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojai, Saskaita, Darbas

class ProjektasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'klientas', 'display_darbuotojai','pradzios_data','pabaigos_data')
    # list_editable = ('pradzios_data','pabaigos_data')
    search_fields = ('id', 'pavadinimas')

class KlientasAdmin(admin.ModelAdmin):
    list_display = ('vardas', 'pavarde','imone', 'kontaktai')

class DarbuotojaiAdmin(admin.ModelAdmin):
    list_display = ('vardas', 'pavarde', 'pareigos')
    list_editable = ('pareigos',)

class SaskaitaAdmin(admin.ModelAdmin):
    list_display = ('suma', 'israsymo_data')

class DarbasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'pastabos', 'busena')
    list_filter = ('busena',)

# Register your models here.
admin.site.register(Projektas,ProjektasAdmin)
admin.site.register(Klientas,KlientasAdmin)
admin.site.register(Darbuotojai,DarbuotojaiAdmin)
admin.site.register(Saskaita,SaskaitaAdmin)
admin.site.register(Darbas,DarbasAdmin)