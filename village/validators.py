from django.db import models
from django.core.exceptions import ValidationError

#A validator that checks if the id from a medical_ninja _validator belongs to an id from a ninja who dominates a curative technique
def medical_ninja_validator(id_value):
    ninja = Ninja.objects.get(person_id=id_value)
    techniques = ninja.techniques.all()
    for t in techniques:
        if CurativeTechnique.objects.filter(id=t.id):
            return id_value
    raise ValidationError('A medical ninja must have at least one curative technique')


#Technique element validator
def technique_element_validator(element):
    if element in ['air', 'water', 'fire', 'earth']:
        return element
    raise ValidationError('An element must be air, water, fire or earth')


#Technique chakra validator
def technique_chakra_validator(chakra_amount):
    if 0 <= chakra_amount <= 1000000:
        return chakra_amount
    raise ValidationError('Chakra amount must be between 0 and 1000000')


def ninja_chakra_validator(chakra):
    if 0 <= chakra <= 6000000:
        return chakra
    raise ValidationError('Chakra must be between 0 and 1000000')


def attack_technique_attack_range_validator(attack_range):
    if attack_range in ['short', 'middle', 'large']:
        return attack_range
    raise ValidationError('Attack range must be short, middle, or large')


def curative_technique_curing_speed_range_validator(speed):
    if speed in ['slow', 'middle', 'fast']:
        return speed
    raise ValidationError('Curative speed must be slow, middle, fast')


def person_gender_validator(gender):
    if gender in ['M', 'F']:
        return gender
    raise ValidationError('Gender must be M or F')


def exam_grade_validator(grade):
    if 0 <= grade <= 100:
        return grade
    raise ValidationError('Grade must be between 0 and 100')


def yen_validator(yens):
    if 0 <= yen <= 100000000:
        return yen
    raise ValidationError('Yens must be between 0 and 100000000')


def rank_validator(rank):
    if rank in ['S','A','B','C','D','E']:
        return rank
    raise ValidationError('Rank must be S,A,B,C,D, or E')


def amount_validator(amount):
    if 0 <= amount <= 1000:
        return yen
    raise ValidationError('Amount must be between 0 and 1000')
