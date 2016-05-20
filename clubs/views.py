from django.shortcuts import render
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from .models import Club
from django.views.generic import View
from .forms import ClubForm



def my_club(request):
    club, created = Club.objects.get_or_create(president=request.user)
    return render(request, "club/club.html", {"club": club})




class EditClub(View):
    template_name = "club/edit.html"
    form = ClubForm


    def get(self, request):
        my_club = Club.objects.get(president=request.user)
        form = self.form(instance=my_club)
        context = {'my_club':my_club, 'form':form}
        return render(request, self.template_name, context)


    def post(self, request):
        pass
