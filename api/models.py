from django.db import models

# Create your models here.
# from .serializers import SiteSerializer

import uuid
from django.contrib.auth.models import AbstractUser
def generate_unique_id():
    return str(uuid.uuid4())



class User(AbstractUser):
    id = models.CharField(primary_key=True, default=generate_unique_id, editable=False, max_length=36)
    is_team_manager = models.BooleanField(default=False)
    country = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254, unique=True)
    RULES_CHOICES = [
        ('Chef de délégation','Chef de délégation'),
        ('Jury / Organisme de contrôle','Jury / Organisme de contrôle'),
        ('Media','Media')
    ]
    rule = models.CharField(max_length=50, choices=RULES_CHOICES, default='Chef de délégation')

class Participant(models.Model):
    id = models.CharField(primary_key=True, default=generate_unique_id, editable=False, max_length=36)
    name = models.CharField(max_length=50)
    surname = models.CharField( max_length=50)
    photo = models.TextField()
    CATEGORIES_CHOICES = [
        ('Haute Personnalité','Haute Personnalité'),
        ('Invité','Invité'),
        ('Jury et organisme de contrôle','Jury et organisme de contrôle'),
        ('Délégation','Délégation'),
        ('Organisation','Organisation'),
        ('Presse','Presse'),
        ('Radio télé difiseur','Radio télé difiseur'),
        ('Bénévole','Bénévole'),
        ]
    FUNCTION_CHOICES = [
        ('Haute Personnalité', 'Haute Personnalité'),
        ('Invité', 'Invité'),
        ('Président du jury', 'Président du jury'),
        ('Délégation technique sportif', 'Délégation technique sportif'),
        ('Officiel sport', 'Officiel sport'),
        ('Juré culturel', 'Juré culturel'),
        ('Antidopage', 'Antidopage'),
        ('Officiel', 'Officiel'),
        ('Membre du gouvernement', 'Membre du gouvernement'),
        ('Chef de délagation', 'Chef de délagation'),
        ('Chef de mission', 'Chef de mission'),
        ('Administrateif', 'Administrateif'),
        ('Entraîneur', 'Entraîneur'),
        ('Technique', 'Technique'),
        ('Médical', 'Médical'),
        ('Compétiteur', 'Compétiteur'),
        ('CNJF', 'CNJF'),
        ('Officile-Org', 'Officile-Org'),
        ('CIJF', 'CIJF'),
        ('Responsable de site', 'Responsable de site'),
        ('Reponsable d\'activité', 'Reponsable d\'activité'),
        ('Sécurité', 'Sécurité'),
        ('Organisateur', 'Organisateur'),
        ('Presse', 'Presse'),
        ('Média télé-radio', 'Média télé-radio'),
        ('Bénévole', 'Bénévole'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES)
    function = models.CharField(max_length=50, choices = FUNCTION_CHOICES)
    country = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    parent = models.ForeignKey("User",  on_delete=models.SET_NULL,blank=True, null=True)


