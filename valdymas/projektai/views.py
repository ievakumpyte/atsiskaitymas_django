from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Projektas, Klientas, Darbuotojai, Darbas, Saskaita
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required

def index(request):
    projektu_kiekis = Projektas.objects.all().count()
    darbuotoju_kiekis = Darbuotojai.objects.all().count()
    klientu_kiekis = Klientas.objects.all().count()


    context = {
        'projektu_kiekis': projektu_kiekis,
        'darbuotoju_kiekis': darbuotoju_kiekis,
        'klientu_kiekis': klientu_kiekis,
    }
    return render(request, 'index.html', context=context)


class ProjektasListView(generic.ListView):
    model = Projektas
    paginate_by = 3
    template_name = 'projektai.html'


class ProjectDetailView(generic.DetailView):
    model = Projektas
    template_name = 'projektas.html'

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.object.id})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password, first_name=name,
                                             last_name=surname)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

class UserProjectsListView(LoginRequiredMixin, generic.ListView):
    model = Projektas
    template_name = 'user_projects.html'
    paginate_by = 3

    def get_queryset(self):
        return Projektas.objects.filter(vadovas=self.request.user).order_by('pavadinimas')