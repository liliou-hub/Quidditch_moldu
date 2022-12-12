from django.shortcuts import render
from .models import Ligue,Equipe,Match

def index(request):
    list_ligue = Ligue.objects.all()
    context = {
        'list_ligue': list_ligue
    }
    return render(request, 'ligues/index.html', context)

def detail(request, question_id):
    question = Ligue.objects.get(pk=question_id)  
    cards = [
    {
        "id":question_id ,
        "name": "Gryffondor",
        "image": "g.jpg",
        "description": "Equipe Gryffondor.",
        
    },
        
    {
        "id": question_id,
        "name": "Serpentar",
        "image": "serp.jpg",
        "description": "Equipe Serpentar.",
        
    },
     
    {
        "id": question_id,
        "name": "Poutsouffle",
        "image": "p.jpg",
        "description": "Equipe Poutsouffle.",
        
    },
    
    {
        "id": question_id,
        "name": "Serdaigle",
        "image": "serd.jpg",
        "description": "Equipe Serdaigle.",
        
    },
    
    ]
    
    context0={
        "cards": cards,
        'question': question,
    }
    return render(request, 'ligues/detail.html', context0)

def results(request, equipe_id):
    
    equipe = Equipe.objects.get(pk=equipe_id)
    matchs=Match.objects.all().filter(locaux=equipe_id) |Match.objects.all().filter(visiteur=equipe_id) 
    date__=Match.objects.all()
    print('lilia',len(matchs))
    context1={       
        'list_match':  matchs,
        'equipe':equipe,
        'date':date__     
    }
    return render(request, 'ligues/results.html', context1)

def classement(request,ligue_id):
    ligue=Ligue.objects.get(pk=ligue_id)
    context={
        'ligue':ligue
    }
    return render (request, 'ligues/classement.html',context)

    

    


