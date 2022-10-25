from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Projektas, Klientas, Darbuotojai, Darbas, Saskaita

def index(request):

    return render(request, 'index.html')


def projects(request):
    paginator = Paginator(Projektas.objects.all(), 1)
    page_number = request.GET.get('page')
    paged_projects = paginator.get_page(page_number)
    projektai = Projektas.objects.all()
    context = {
        'projektai': paged_projects
    }
    return render(request, 'projektai.html', context=context)

def project(request, project_id):
    single_project = get_object_or_404(Projektas, pk=project_id)
    saskaitos = Saskaita.objects.filter(projektas=project_id)
    context = {
        'project': single_project,
        'sask': saskaitos
    }

    return render(request, 'projektas.html', context=context)

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
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
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')