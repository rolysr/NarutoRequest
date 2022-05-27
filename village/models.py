from django.db import models

# Create your models here.


class Invocation(models.Model):
    name_i = models.CharField(max_length=30)
    type_i = models.CharField(max_length=20)


class Technique(models.Model):
    element = models.CharField(max_length=20)
    is_hidden = models.BooleanField()
    chakra_amount = models.IntegerField()


class AttackTechnique(models.Model):
    technique = models.OneToOneField(Technique, null=False, blank=False, on_delete=models.CASCADE)
    attack_range = models.CharField(max_length=5) #short, middle, large


class CurativeTechnique(models.Model):
    technique = models.OneToOneField(Technique, null=False, blank=False, on_delete=models.CASCADE)
    curing_speed = models.CharField(max_length=5) #slow, middle, fast


class Person(models.Model):
    name_p = models.CharField(max_length=30)
    gender = models.CharField(max_length=1) #M o F
    clan = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    age = models.IntegerField()


class Ninja(models.Model):
    person = models.OneToOneField(Person, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    max_chakra_amount = models.IntegerField()
    techniques = models.ManyToManyField(Technique)
    invocations = models.ManyToManyField(Invocation)


class Genin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    assessment = models.TextField()
    g_date = models.DateField()


class Chunin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    chunin_exam_grade = models.IntegerField() #Asumimos en base a 100
    c_date = models.DateField()


class Jounin(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    jounin_exam_grade = models.IntegerField() #Asumimos en base a 100
    j_date = models.DateField()


class MedicalNinja(models.Model):
    ninja = models.OneToOneField(Ninja, primary_key=True, null=False, blank=False, on_delete=models.CASCADE) 


class Parchment(models.Model):
    sealed_date = models.DateField()
    ninja = models.ForeignKey(Ninja, null=False, blank=False, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, null=False, blank=False, on_delete=models.CASCADE)


class Client(models.Model):
    name_c = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class Team(models.Model):
    name_t = models.CharField(max_length=30)
    medical_ninja = models.OneToOneField(MedicalNinja, null=False, blank=False, on_delete=models.CASCADE)
    members = models.ForeignKey(Ninja, null=False, blank=False, on_delete=models.CASCADE)


class Mission(models.Model):
    captain = models.OneToOneField(Jounin, null=False, blank=False, on_delete=models.CASCADE)
    i_date = models.DateField()
    f_date = models.DateField()
    satisfactory_result = models.BooleanField()
    reward_yens = models.IntegerField()
    rank_m = models.CharField(max_length=1)
    client = models.OneToOneField(Client, null=False, blank=False, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, null=False, blank=False, on_delete=models.CASCADE)
    parchments = models.ManyToManyField(Parchment)
    churikens_amount = models.IntegerField()
    kunais_amount = models.IntegerField()
    explosive_seals_amount = models.IntegerField()
