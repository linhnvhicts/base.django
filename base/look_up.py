from django.shortcuts import render
from django.db.models import Q
from dal import autocomplete
from django.contrib.auth.models import User

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all().filter()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)) 

        return qs