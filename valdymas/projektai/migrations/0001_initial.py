# Generated by Django 4.1.1 on 2022-10-17 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Darbas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('pastabos', models.CharField(max_length=100, verbose_name='Pastabos')),
            ],
            options={
                'verbose_name': 'Darbas',
                'verbose_name_plural': 'Darbai',
            },
        ),
        migrations.CreateModel(
            name='Darbuotojai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vardas', models.CharField(max_length=100, verbose_name='Vardas')),
                ('pavarde', models.CharField(max_length=100, verbose_name='Pavardė')),
                ('pareigos', models.CharField(max_length=100, verbose_name='Pareigos')),
            ],
            options={
                'verbose_name': 'Darbuotojas',
                'verbose_name_plural': 'Darbuotojai',
            },
        ),
        migrations.CreateModel(
            name='Klientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vardas', models.CharField(max_length=100, verbose_name='Vardas')),
                ('pavarde', models.CharField(max_length=100, verbose_name='Pavardė')),
                ('imone', models.CharField(max_length=100, verbose_name='Įmonė')),
                ('kontaktai', models.CharField(max_length=100, verbose_name='Kontaktai')),
            ],
            options={
                'verbose_name': 'Klientas',
                'verbose_name_plural': 'Klientai',
            },
        ),
        migrations.CreateModel(
            name='Saskaita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('israsymo_data', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('suma', models.FloatField(verbose_name='Suma')),
            ],
            options={
                'verbose_name': 'Sąskaita',
                'verbose_name_plural': 'Sąskaitos',
            },
        ),
        migrations.CreateModel(
            name='Projektas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('pradzios_data', models.DateField(blank=True, null=True, verbose_name='Pradžios data')),
                ('pabaigos_data', models.DateField(blank=True, null=True, verbose_name='Pabaigos data')),
                ('darbai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projektai.darbas')),
                ('darbuotojai', models.ManyToManyField(to='projektai.darbuotojai')),
                ('klientas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projektai.klientas')),
                ('saskaitos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projektai.saskaita')),
                ('vadovas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Projektas',
                'verbose_name_plural': 'Projektai',
            },
        ),
    ]