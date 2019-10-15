from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "tv_shows_app/shows.html", { "all_shows": Show.objects.all()} )

def show_profile(request, show_id):
    return render(request, "tv_shows_app/show_prof.html", {"this_show": Show.objects.get(id=show_id)})

def edit_show(request, show_id):
    return render(request, "tv_shows_app/edit_show.html", {"this_show": Show.objects.get(id=show_id)})

def new_show(request):
    return render(request, "tv_shows_app/new_show.html")

def add_show_from_form(request):
    errors = Show.objects.basic_validator(request.POST)
    print(errors)
    print(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:    
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        newShow = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        newShow.save()
        newShow_id = newShow.id
        return redirect('/shows/' + str(newShow_id))

def update_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    errors = Show.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/' + show_id + '/edit')
    else: 
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect('/shows/' + show_id)

def delete_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()
    return redirect('/shows')


