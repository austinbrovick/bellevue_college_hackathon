from django.shortcuts import render
from django.http import HttpResponse


from tags.models import Tag
from clubs.models import Club


def info(request):
    tag_count = 0
    connections = []
    tags = Tag.objects.filter(profile=request.user.profile)
    clubs = Club.objects.all()

    club = Club.objects.first()
    abc = club.tags.all()
    for x in abc:
        print(x)


    for tag_from_me in tags:
        for club in clubs:
            for tag_from_club in club.tags.all():
                print("$$$$$$$$$$$$")
                print(tag_from_club)
                print(tag_from_me)
                print("$$$$$$$$$$$$")
                if tag_from_club.name == tag_from_me.name:
                    connections.append(club)
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
    return render(request, "info/info.html", {"connections":unique_connections})















    return render(request, 'info/info.html')
    # return HttpResponse("hello")

