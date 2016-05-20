from django.shortcuts import render, redirect
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from .models import Club
from django.views.generic import View
from .forms import ClubForm
from tags.forms import SearchTagForm
from tags.models import Tag
from profiles.models import Profile
from django.http import HttpResponse



def my_club(request):
    connections = []
    club, created = Club.objects.get_or_create(president=request.user)
    tags = Tag.objects.filter(club=club)
    profiles = Profile.objects.all()


    for tag_from_club in tags:
        for profile in profiles:
            for tag_from_user in profile.tags.all():
                if tag_from_user.name == tag_from_club.name:
                    connections.append(profile)

    print(connections)
    unique_connections = []

    for x in connections:
        status = True
        for y in unique_connections:
            if x == y:
                status = False
        if status == True:
            unique_connections.append(x)

    print(unique_connections)
    return render(request, "club/club.html", {"club": club, "form":SearchTagForm(), 'tags':tags, 'connections':unique_connections})




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


def clubs(request):
    clubs = Club.objects.all()
    context = {'clubs':clubs}
    return render(request, "club/clubs.html", context)


def club_profile(request, pk):
    club = Club.objects.get(pk=pk)
    tags = Tag.objects.filter(club=club)
    return render(request, 'club/club_page.html', {'club' : club, 'tags':tags})
