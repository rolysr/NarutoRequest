from django.db import models
from django.core.exceptions import ValidationError
from village.validators import *

# Create your models here.

class Invocation(models.Model):
    name_i = models.CharField(max_length=30)
    type_i = models.CharField(max_length=20)
    def __str__(self):
        return self.name_i + '({0})'.format(self.id)


class Technique(models.Model):
    name = models.CharField(max_length=30)
    element = models.CharField(max_length=20, validators=[technique_element_validator])
    is_hidden = models.BooleanField()
    chakra_amount = models.IntegerField(validators=[technique_chakra_validator])
    def __str__(self):
        return self.name + '({0})'.format(self.id)


class AttackTechnique(models.Model):
    technique = models.OneToOneField(Technique, null=False, blank=False, on_delete=models.CASCADE)
    attack_range = models.CharField(max_length=5, validators=[attack_technique_attack_range_validator]) #short, middle, large
    def __str__(self):
        return self.technique.name + '({0})'.format(self.technique.id)


class CurativeTechnique(models.Model):
    technique = models.OneToOneField(Technique, null=False, blank=False, on_delete=models.CASCADE)
    curing_speed = models.CharField(max_length=5, validators=[curative_technique_curing_speed_range_validator]) #slow, middle, fast
    def __str__(self):
        return self.technique.name + '({0})'.format(self.technique.id)


class Person(models.Model):
    name_p = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, validators=[person_gender_validator]) #M o F
    clan = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    def __str__(self):
        return self.name_p + '({0})'.format(self.id)


class Ninja(models.Model):
    person = models.OneToOneField(Person, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    max_chakra_amount = models.IntegerField(validators=[ninja_chakra_validator])
    techniques = models.ManyToManyField(Technique)
    invocations = models.ManyToManyField(Invocation)
    def __str__(self):
        return self.person.name_p + '({0})'.format(self.person.id)


class Genin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    assessment = models.TextField()
    g_date = models.DateField()
    def __str__(self):
        return self.ninja.person.name_p + '({0})'.format(self.ninja.person.id)


class Chunin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    chunin_exam_grade = models.IntegerField(validators=[exam_grade_validator]) #Asumimos en base a 100
    c_date = models.DateField()
    def __str__(self):
        return self.ninja.person.name_p + '({0})'.format(self.ninja.person.id)


class Jounin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    jounin_exam_grade = models.IntegerField(validators=[exam_grade_validator]) #Asumimos en base a 100
    j_date = models.DateField()
    def __str__(self):
        return self.ninja.person.name_p + '({0})'.format(self.ninja.person.id)


class MedicalNinja(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE, validators=[medical_ninja_validator]) 
    def __str__(self):
        return self.ninja.person.name_p + '({0})'.format(self.ninja.person.id)
    

class Parchment(models.Model):
    sealed_date = models.DateField()
    ninja = models.ForeignKey(Ninja, null=False, blank=False, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return 'Seal made by ' + self.ninja.person.name_p + 'with technique {1} '.format(str(self.technique.name)) + '({0})'.format(self.ninja.person.id)
    

class Client(models.Model):
    name_c = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.name_c + '({0})'.format(self.ninja.person.id)


class Team(models.Model):
    name_t = models.CharField(max_length=30)
    medical_ninja = models.OneToOneField(MedicalNinja, null=False, blank=False, on_delete=models.CASCADE)
    members = models.ForeignKey(Ninja, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_t + '({0})'.format(self.id)


class Mission(models.Model):
    captain = models.OneToOneField(Jounin, null=False, blank=False, on_delete=models.CASCADE)
    i_date = models.DateField()
    f_date = models.DateField()
    satisfactory_result = models.BooleanField()
    reward_yens = models.IntegerField(validators=[yen_validator])
    rank_m = models.CharField(max_length=1, validators=[rank_validator])
    client = models.OneToOneField(Client, null=False, blank=False, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, null=False, blank=False, on_delete=models.CASCADE)
    parchments = models.ManyToManyField(Parchment)
    churikens_amount = models.IntegerField(validators=[amount_validator])
    kunais_amount = models.IntegerField(validators=[amount_validator])
    explosive_seals_amount = models.IntegerField(validators=[amount_validator])
    def __str__(self):
        return 'Mission with team {0} for client {1}'.format(self.team, self.client)
