from django.contrib import admin
from .models import Etudiant

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'matricule', 'ue', 'professeur')
    search_fields = ('nom', 'prenom', 'matricule')