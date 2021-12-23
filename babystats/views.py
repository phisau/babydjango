from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category, Event
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.template import loader

# Create your views here.

def index(request):
    latest_category_list = Category.objects.order_by('-pub_date')[:5]
    template = loader.get_template('babystats/index.html')
    context = {
            'latest_category_list': latest_category_list,
            }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    latest_category_list = Category.objects.order_by('-pub_date')[:5]
    latest_event_list = Event.objects.order_by('-event_text')[:5]
    template = loader.get_template('babystats/dashboard.html')
    context = {
            'latest_category_list': latest_category_list,
            'latest_event_list': latest_event_list,
            }
    return HttpResponse(template.render(context, request))

def click(request):
    return HttpResponse("Click what's happening")


def detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("category does not exist")
    return render(request, 'babystats/detail.html', {'category': category})


def results(request, category_id):
    response = "You're looking at the results of category %s."
    return HttpResponse(response % category_id)


def vote(request, category_id):
    return HttpResponse("You're voting on category%s." % category_id)

def running(request, category_id, event_id):
    category = get_object_or_404(Category, pk=category_id)
#    event = get_object_or_404(Event, pk=event_id)
    event = get_object_or_404(Event, pk=event_id)
    
    return render(request, 'babystats/running.html', {'category': category, 'event': event})

def saveme(request, category_id, event_id):
    print(request.POST)
    time_from = request.POST['event_from']
    time_to = request.POST['event_to']
    mood = request.POST['mood']
    print("saveme") 
    category = get_object_or_404(Category, pk=category_id)
    event = get_object_or_404(Event, pk=event_id)
    event.time_from = time_from
    event.time_to = time_to
    event.mood = mood 
#    event = category.event_set.create()

    if request.POST['action'] == 'End':
        event.save()
        return HttpResponseRedirect(reverse('babystats:dashboard'))
    else:
        event.time_to = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        event.save()
        return render(request, 'babystats/running.html', {'category': category, 'event': event})

def end_event(request, category_id, event_id):
    print(request.POST)
    time_from = request.POST['event_from']
    time_to = request.POST['event_to']
    mood = request.POST['mood']
    print("saveme") 
    category = get_object_or_404(Category, pk=category_id)
    event = get_object_or_404(Event, pk=event_id)
    event.time_from = time_from
    event.time_to = time_to
    event.mood = mood 
    event.save()
#    event = category.event_set.create()
    print(80*'-')
    #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponseRedirect(reverse('babystats:dashboard'))
#    return HttpResponseRedirect(request, 'babystats/dashboard.html', )



def create_new(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    event = category.event_set.create()

    return render(request, 'babystats/running.html', {'category': category, 'event': event})
