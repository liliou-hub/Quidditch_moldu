from django.contrib import admin

from .models import Ligue
from .models import Equipe
from .models import Match
from .models import Joueur

admin.site.register(Ligue)
admin.site.register(Equipe)
admin.site.register(Joueur)
admin.site.register(Match)