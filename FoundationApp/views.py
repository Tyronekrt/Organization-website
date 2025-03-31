from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from FoundationApp.forms import ImageModelForm, EventModelForm
from FoundationApp.models import ImageModel, EventModel, UserModel


def index(request):
    events = EventModel.objects.all()
    members = ImageModel.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'members': members,
    })

def starter(request):
    events = EventModel.objects.all()
    return render(request, 'starter-page.html', {'events': events})

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

def upload_view(request):
    if request.method == 'POST':
        if 'eventimage' in request.FILES:
            # Handling event image upload
            event_image = request.FILES.get('eventimage')
            EventModel.objects.create(eventimage=event_image)
            return redirect('events')

        if 'memberimage' in request.FILES and 'membername' in request.POST:
            # Handling team member upload
            member_name = request.POST.get('membername')
            position = request.POST.get('position')
            member_image = request.FILES.get('memberimage')
            ImageModel.objects.create(membername=member_name, position=position, memberimage=member_image)
            return redirect('teams')

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
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserModel.objects.get(email=username, password=password)
            request.session['user_id'] = user.id
            request.session['logged_in'] = True  # Add session flag
            return redirect('uploadview')
        except UserModel.DoesNotExist:
            messages.error(request, 'Invalid credentials!!!')
            return redirect('login')
    else:
        # If already logged in, redirect to uploadview
        if request.session.get('logged_in'):
            return redirect('uploadview')
        return render(request, 'log-in.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def uploadimage(request):
    # Check session authentication
    if not request.session.get('logged_in'):
        return redirect('login')
    # Your existing uploadview logic
    return render(request, 'upload_image.html')

def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('login')


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

def editevents(request, id):
    editevents = EventModel.objects.get(id = id)
    return render(request,'editevents.html',{
        'editevents': editevents
    })

def updatevents(request, id):
    updatevents = EventModel.objects.get(id=id)
    form = EventModel(request.POST, instance=updatevents)
    if form.is_valid():
        form.save()
        return redirect('/events')
    else:
        return render(request, 'editevents.html')


def deletemembers(request, id):
    member = ImageModel.objects.get(id=id)
    member.delete()
    return redirect('/adminmember')

def deleteevents(request, id):
    event = EventModel.objects.get(id=id)
    event.delete()
    return redirect('/adminevents')



#
# def logout_view(request):
#     logout(request)
#     request.session.flush()
#     return redirect('index')
