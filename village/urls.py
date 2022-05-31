from django.urls import path
from . import views


app_name = 'village'
urlpatterns = [
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
]
