from http import client
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Count, Sum, Avg, Subquery, OuterRef, Q
from django.views.generic import ListView, FormView
from village.models import *


# Create your views here.


class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request):
        return render(request, self.template_name)


class PersonList(ListView):
    ordering = ['id']
    model = Person
    template_name = 'persons/index.html'
    paginate_by = 5


class NinjaList(ListView):
    ordering = ['person_id']
    model = Ninja
    template_name = 'ninjas/ninja.html'
    paginate_by = 5


class MedicalNinjaList(ListView):
    ordering = ['ninja_id']
    model = MedicalNinja
    template_name = 'ninjas/medical_ninja.html'
    paginate_by = 5

class GeninList(ListView):
    ordering = ['ninja_id']
    model = Genin
    template_name = 'ninjas/genin.html'
    paginate_by = 5


class ChuninList(ListView):
    ordering = ['ninja_id']
    model = Chunin
    template_name = 'ninjas/chunin.html'
    paginate_by = 5


class JouninList(ListView):
    ordering = ['ninja_id']
    model = Jounin
    template_name = 'ninjas/jounin.html'
    paginate_by = 5


class ClientList(ListView):
    ordering = ['-id']
    model = Client
    template_name = 'missions/client.html'
    paginate_by = 5


class MissionList(ListView):
    ordering = ['id']
    model = Mission
    template_name = 'missions/mission.html'
    paginate_by = 5


class TeamList(ListView):
    ordering = ['id']
    model = Team
    template_name = 'teams/team.html'
    paginate_by = 5


class TechniqueList(ListView):
    ordering = ['id']
    model = Technique
    template_name = 'others/technique.html'
    paginate_by = 5


class AttackList(ListView):
    ordering = ['technique_id']
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


class Query1List(ListView):
    ordering = ['-ninja_id']
    model = MedicalNinja
    template_name = 'queries/medical_gender/medical_gender.html'
    paginate_by = 5
    def get(self, request):
        total = len(self.model.objects.all()) 
        women_number = len(self.model.objects.filter(ninja__person__gender='F'))
        men_number = len(self.model.objects.filter(ninja__person__gender='M'))
        context = {
            'object_list': self.model.objects.all(),
            'women_percent': str(100*(women_number/total)) + '%',
            'men_percent': str(100*(men_number/total)) + '%',
            'values': request.GET
        }

        return render(request, self.template_name, context)


class Query2List(ListView):
    ordering = ['-ninja_id']
    model = Mission
    template_name = 'queries/captain_mission/captain_mission.html'
    paginate_by = 5
    def get(self, request):
        context = None
        minimum_rank = None
        number_missions = None
        try:    
            minimum_rank = request.GET['selected_rank'][0]
            number_missions = int(request.GET['number_missions']) if request.GET['number_missions']!='' else 0
        except:
            minimum_rank = 'F'
            number_missions = 0

        if minimum_rank != 'S':
            query_model = self.model.objects.all().filter((Q(rank_m__lte=minimum_rank) & Q(rank_m__gte='A')) | Q(rank_m='S')).select_related('captain').values('captain', 'captain__ninja__person__name_p').annotate(Count('id')).filter(Q(id__count__gte=number_missions))
        else: 
            query_model = self.model.objects.all().filter(Q(rank_m='S')).select_related('captain').values('captain', 'captain__ninja__person__name_p').annotate(Count('id')).filter(Q(id__count__gte=number_missions))
        context = {
            'object_list': query_model,
            'values' : request.GET 
        }
        return render(request, self.template_name, context)


class Query3List(ListView):
    ordering = ['reward_yens']
    model = Mission
    template_name = 'queries/ninja_invocation_mission/ninja_invocation_mission.html'
    paginate_by = 5
    def get(self, request):
        context = None
        minimum_rank = None
        number_missions = None
        try:    
            minimum_rank = request.GET['selected_rank'][0]
            number_missions = int(request.GET['number_missions']) if request.GET['number_missions']!='' else 0
        except:
            minimum_rank = 'F'
            number_missions = 0
        if minimum_rank != 'S':
            query_model = self.model.objects.all().filter((Q(rank_m__lte=minimum_rank) & Q(rank_m__gte='A')) | Q(rank_m='S')).select_related('team').values('team__members__person_id', 'team__members__person__name_p', 'team__members__person__clan', 'team__members__invocations__id', 'team__members__invocations__name_i').annotate(Count('id')).filter(Q(id__count__gte=number_missions))
        else:
            query_model = self.model.objects.all().filter(Q(rank_m='S')).select_related('team').values('team__members__person_id', 'team__members__person__name_p', 'team__members__person__clan', 'team__members__invocations__id', 'team__members__invocations__name_i').annotate(Count('id')).filter(Q(id__count__gte=number_missions))
        print(query_model)
        context = {
            'object_list': query_model,
            'values' : request.GET 
        }
        return render(request, self.template_name, context)


class Query4List(ListView):
    ordering = ['reward_yens']
    model = Mission
    template_name = 'queries/technique_mission/technique_mission.html'
    paginate_by = 5
    def get(self, request):
        query_model = self.model.objects.all().filter(~Q(client__country='Fire Country')).select_related('team').values('team__members__techniques__id', 'team__members__techniques__name', 'team__members__techniques__is_hidden').annotate(Count('id'))

        for i in range(len(query_model)):
            q = query_model[i]
            tech_id = q['team__members__techniques__id']
            aux_query = self.model.objects.all().filter(~Q(client__country='Fire Country')).select_related('team').values('team__members__techniques__id', 'team__members__techniques__name', 'team__members__techniques__is_hidden', 'client__country').annotate(Count('id'))
            q['countries'] = set()
            for aux_q in aux_query:
                if aux_q['team__members__techniques__id'] == tech_id:
                    q['countries'].add(aux_q['client__country'])
                    
        context = {
            'object_list': query_model,
            'values' : request.GET 
        }
        return render(request, self.template_name, context)


class Query5List(ListView):
    ordering = ['reward_yens']
    model = Mission
    template_name = 'queries/medical_mission/medical_mission.html'
    paginate_by = 5
    def get(self, request):
        query_model = self.model.objects.all().select_related('captain').values('captain__ninja_id', 'captain__ninja__person__name_p').annotate(Count('id'))       
        print(query_model)
        for i in range(len(query_model)):
            cap_id = query_model[i]['captain__ninja_id']
            print(cap_id)
            query_model[i]['is_medical_ninja'] = 'False'
            try:
                medical_n = MedicalNinja.objects.get(ninja_id=str(cap_id))
                query_model[i]['is_medical_ninja'] = 'True'
            except:
                pass
        context = {
            'object_list': query_model,
            'values' : request.GET 
        }
        return render(request, self.template_name, context)


class Query6List(ListView):
    model = Mission
    template_name = 'queries/missions_reward/missions_reward.html'
    paginate_by = 5
    def get(self, request):
        context = None
        ordering_method = None
        display_order = None
        try:    
            ordering_method = request.GET['ordering_method']
            display_order = request.GET['display_order']
        except:
            ordering_method = 'id'
            display_order = 'a'
        
        if display_order == 'a':
            query_model = self.model.objects.all().order_by(ordering_method)
        elif display_order == 'd': 
            query_model = self.model.objects.all().order_by('-'+ordering_method)
        context = {
            'object_list': query_model,
            'values' : request.GET 
        }
        return render(request, self.template_name, context)

        
