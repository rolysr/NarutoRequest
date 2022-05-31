from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView
from village.models import *


# Create your views here.

class PersonList(ListView):
    ordering = ['-id']
    model = Person
    template_name = 'persons/index.html'
    paginate_by = 5


class NinjaList(ListView):
    ordering = ['-person_id']
    model = Ninja
    template_name = 'ninjas/ninja.html'
    paginate_by = 5


class MedicalNinjaList(ListView):
    ordering = ['-ninja_id']
    model = MedicalNinja
    template_name = 'ninjas/medical_ninja.html'
    paginate_by = 5

class GeninList(ListView):
    ordering = ['-ninja_id']
    model = Genin
    template_name = 'ninjas/genin.html'
    paginate_by = 5


class ChuninList(ListView):
    ordering = ['-ninja_id']
    model = Chunin
    template_name = 'ninjas/chunin.html'
    paginate_by = 5


class JouninList(ListView):
    ordering = ['-ninja_id']
    model = Jounin
    template_name = 'ninjas/jounin.html'
    paginate_by = 5


class ClientList(ListView):
    ordering = ['-id']
    model = Client
    template_name = 'missions/client.html'
    paginate_by = 5


class MissionList(ListView):
    ordering = ['-id']
    model = Mission
    template_name = 'missions/mission.html'
    paginate_by = 5


class TeamList(ListView):
    ordering = ['-id']
    model = Team
    template_name = 'teams/team.html'
    paginate_by = 5


class TechniqueList(ListView):
    ordering = ['-id']
    model = Technique
    template_name = 'others/technique.html'
    paginate_by = 5


class AttackList(ListView):
    ordering = ['-technique_id']
    model = AttackTechnique
    template_name = 'others/attack.html'
    paginate_by = 5


class CurativeList(ListView):
    ordering = ['-technique_id']
    model = CurativeTechnique
    template_name = 'others/curative.html'
    paginate_by = 5


class ParchmentList(ListView):
    ordering = ['-id']
    model = Parchment
    template_name = 'others/parchment.html'
    paginate_by = 5


class InvocationList(ListView):
    ordering = ['-id']
    model = Invocation
    template_name = 'others/invocation.html'
    paginate_by = 5
