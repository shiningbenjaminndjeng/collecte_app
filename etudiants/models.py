from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    sexe = models.CharField(max_length=10)
    ethnie = models.CharField(max_length=100)
    ue = models.CharField(max_length=100)
    professeur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"