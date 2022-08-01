from django.urls import path
from . import views


app_name = 'village'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('person', views.PersonList.as_view(), name='person'),

    path('ninjas/ninja', views.NinjaList.as_view(), name='ninja'),
    path('ninjas/medical', views.MedicalNinjaList.as_view(), name='medical'),
    path('ninjas/genin', views.GeninList.as_view(), name='genin'),
    path('ninjas/chunin', views.ChuninList.as_view(), name='chunin'),
    path('ninjas/jounin', views.JouninList.as_view(), name='jounin'),

    path('missions/mission', views.MissionList.as_view(), name='mission'),
    path('missions/client', views.ClientList.as_view(), name='client'),

    path('team', views.TeamList.as_view(), name='team'),
    
    path('others/technique', views.TechniqueList.as_view(), name='technique'),
    path('others/attack', views.AttackList.as_view(), name='attack'),
    path('others/curative', views.CurativeList.as_view(), name='curative'),
    path('others/parchment', views.ParchmentList.as_view(), name='parchment'),
    path('others/invocation', views.InvocationList.as_view(), name='invocation'),

    path('queries/medical-gender', views.Query1List.as_view(), name='medical_gender'),
    path('queries/captain-mission', views.Query2List.as_view(), name='captain_mission'),
    path('queries/ninja-invocation-mission', views.Query3List.as_view(), name='ninja_invocation_mission'),
    path('queries/technique-mission', views.Query4List.as_view(), name='technique_mission'),
    path('queries/medical-mission', views.Query5List.as_view(), name='medical_mission'),
    path('queries/missions-reward', views.Query6List.as_view(), name='missions_reward'),
]
