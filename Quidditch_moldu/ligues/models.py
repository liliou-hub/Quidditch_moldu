from django.db import models



class Ligue(models.Model):
    nom_ligue = models.CharField(max_length=20, default='ligue')
    
    def __str__(self):
        return self.nom_ligue
    
    def get_classement(self):
        equipes = Equipe.objects.all().filter(ligue=self.id)
        for equipe in equipes :
            points = 0
            matches=Match.objects.all().filter(locaux = equipe.id) |Match.objects.all().filter(visiteur=equipe.id)
            for match in matches:
                if match.but_loc> match.but_vis:
                    points +=3   
                elif match.but_loc < match.but_vis:
                    points +=0                 
                elif match.but_loc == match.but_vis :
                    points +=1 
            equipe.points = points             
            equipe.save()
        return equipes.order_by('points').reverse()
            
class Equipe(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    nom_equipe = models.CharField(max_length=20, default='equipe')
    img=models.CharField(max_length=100, default='img')
    points=models.IntegerField(max_length=100,default=0)
    
    def __str__(self):
        return self.nom_equipe
    
       
class Joueur(models.Model):
    nom_equipe=models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nom_joueur=models.CharField(max_length=20,default='nom_joueur')
    
    def __str__(self):
        return self.nom_joueur
        
    
class Match(models.Model):
    ligue=models.ForeignKey(Ligue, on_delete=models.CASCADE)
    locaux=models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name="locaux")
    but_loc=models.IntegerField(default=0)
    visiteur=models.ForeignKey(Equipe, on_delete=models.CASCADE,related_name="visiteur")
    but_vis=models.IntegerField(default=0)
    nom_match= models.CharField(max_length=100, default='nom_match')
    date_match = models.DateField('Date du match',null=True)
    img_loc=models.CharField(max_length=100, default='img_loc')
    img_vis=models.CharField(max_length=100, default='img_vis')
    
    def __str__(self):
        return self.nom_match
    
    
   
   