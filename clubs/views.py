from django.shortcuts import render, redirect
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from .models import Club
from django.views.generic import View
from .forms import ClubForm
from tags.forms import SearchTagForm



def my_club(request):
    club, created = Club.objects.get_or_create(president=request.user)
    return render(request, "club/club.html", {"club": club, "form":SearchTagForm()})




class EditClub(View):
    template_name = "club/edit.html"
    form = ClubForm


    def get(self, request):
        my_club = Club.objects.get(president=request.user)
        form = self.form(instance=my_club)
        context = {'my_club':my_club, 'form':form}
        return render(request, self.template_name, context)


    def post(self, request):
        my_club, created = Club.objects.get_or_create(president=request.user)
        form = self.form(request.POST or None, request.FILES or None, instance=my_club)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.president = request.user
            instance.save()
            return redirect("my_club")
        else:
            return redirect("edit_club")
