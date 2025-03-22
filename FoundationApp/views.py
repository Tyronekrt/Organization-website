from django.shortcuts import render
from django.views.generic import detail


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
