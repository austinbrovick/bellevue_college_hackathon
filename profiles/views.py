from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from .forms import ProfileForm
from tags.models import Tag
from tags.forms import SearchTagForm
from django.contrib.auth.decorators import login_required


def my_profile(request):
    my_profile, created = Profile.objects.get_or_create(user=request.user)
    me = request.user
    tags = Tag.objects.filter(profile=request.user.profile)
    context = {
        "my_profile" : me,
        'tags' : tags,
        'form' : SearchTagForm()
    }
    return render(request, "profiles/my_profile.html", context)


class EditProfile(View):
    template_name = "profiles/edit.html"
    form = ProfileForm


    def get(self, request):
        print("made it to edit page")
        my_profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form(instance=my_profile)
        context = {'my_profile':my_profile, 'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        my_profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form(request.POST or None, request.FILES or None, instance=my_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("profile")
        else:
            return redirect("edit_profile")


def their_profile(request, pk):
    x = Profile.objects.get(pk=pk)
    my_profile = x.user
    tags = Tag.objects.filter(profile=request.user.profile)
    return render(request, 'profiles/their_profile.html', {'my_profile':my_profile, 'tags':tags})

