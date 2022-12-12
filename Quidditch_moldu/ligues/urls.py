from django.urls import path

from . import views

app_name = 'ligue_sportive'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), 
    path('<int:equipe_id>/results', views.results, name='resultats'),
    path('<int:ligue_id>/results/classement', views.classement, name='classement')
]