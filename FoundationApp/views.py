from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import detail

from FoundationApp.forms import ImageModelForm, EventModelForm
from FoundationApp.models import ImageModel, EventModel


def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'About.html')

def causes(request):
    return render(request, 'causes.html')

def events(request):
    return render(request, 'events.html')

def donate_for_love(request):
    return render(request, 'donate_for_love.html')

def teams(request):
    return render(request, 'teams.html')

def love_for_humanity(request):
    return render(request, 'love_for_humanity.html')

def love_for_future_generations(request):
    return render(request, 'love_for_future_generations.html')

def love_for_environment(request):
    return render(request, 'love_for_environment.html')

def contact(request):
    return render(request, 'contact.html')

def submit(request):
    return render(request, 'submit.html')

def pay(request):
    return render(request, 'pay.html')

from django.shortcuts import render, redirect
from .models import ImageModel

def upload_image(request):
    if request.method == "POST":
        member = ImageModel(
            name=request.POST.get('name'),
            position = request.POST.get('position'),
            image = request.FILES.get('image')
        )
        member.save()
        return redirect('/teams')
    else:
        return render(request, 'upload_image.html')


def upload_events(request):
    if request.method == "POST":
        event = EventModel(
            image = request.FILES.get('image')
        )
        event.save()
        return redirect('/events')  # Redirect after successful save
    else:
        return render(request, 'upload_image.html')

def show_image(request):
    members = ImageModel.objects.all()
    return render(request, 'teams.html', {'members': members})


def show_events(request):
    events = EventModel.objects.all()
    return render(request, 'events.html', {'events': events})

def administrator(request):
    return render(request, 'admin-members.html')

def login(request):
    return render(request,'log-in.html')

def adminMember(request):
    members = ImageModel.objects.all()
    return render(request, 'admin-members.html',{
        'members': members
    })

def adminEvents(request):
    events = EventModel.objects.all()
    return render(request, 'admin-events.html',{
        'events': events
    })

def editmembers(request, id):
    editmembers = ImageModel.objects.get(id = id)
    return render(request,'editmembers.html',{
        'editmembers': editmembers
    })

def updatemembers(request, id):
    updateinfo = ImageModel.objects.get(id=id)
    form = ImageModelForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/teams')
    else:
        return render(request, 'editmembers.html')


def deletemembers(request, id):
    member = ImageModel.objects.get(id=id)
    member.delete()
    return redirect('/adminmember')

