from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.db.models import Sum, Count
from datetime import datetime, timedelta, timezone

from .models import Person, PushUps
from .forms import pushUpForm

def addPushups(request):
    #dateFieldTOCheck = request.POST.get('date')
    loggedPerson = Person.objects.get(user=request.user)

    form = pushUpForm(initial={'user': loggedPerson})
    if request.method == 'POST':
        form = pushUpForm(request.POST)
        #form = form.save(commit=False)
        if form.is_valid():
            form.user = loggedPerson
            form.save()
            return redirect('/')


    loggedUser = request.user.username
    context = {'form': form, 'loggedUser': loggedUser}
    return render(request, './pushup_form.html', context)


def home(request):
    # finally it should be display  logged user
    if request.user.is_authenticated:
        context = {
            'username': request.user.id,
            'numOfPushUps': 0
        }
    else:
        context = {
            'username': 'ERROR',
            'numOfPushUps': 0
        }

    return render(request, "./home.html", context)

def myhistory(request):
    # finally it should be display  logged user history
    loggedUser = request.user.username

    pushapphistory = (PushUps.objects
                      .filter(user__user__username=loggedUser).order_by('-date')
                      )


    for item in pushapphistory:
        year = item.date.strftime("%Y")
        print("year:", year)
        #month = item.date.strftime("%m")
        #print("month:", month)
        monthname = item.date.strftime('%B')
        print("month name:", monthname)
        day = item.date.strftime("%d")
        print("day:", day)

        day = int(day) + 1
        day = str(day)

        date = day + ' ' + monthname + ' ' + year
        item.date = date

    context = {
        'numOfPushUps_list': pushapphistory,
        'loggedUser': loggedUser
    }
    return render(request, "./myhistory.html", context)

def records(request):
    # finally top5 users repeats in week and top3 users series in moth
    last_week = datetime.now(tz=timezone.utc) - timedelta(days=7)
    TOP5Last7Days = (PushUps.objects
                    .filter(date__gt=last_week)
                    .extra(select={'day': 'date(date)'})
                    .values('user')
                    .annotate(sum=Sum('numOfPushUps')).order_by('-sum'))[:5]

    last_month = datetime.now(tz=timezone.utc) - timedelta(days=30)
    TOP3Last30Days = (PushUps.objects
                    .filter(date__gt=last_month)
                    .extra(select={'day': 'date(date)'})
                    .values('user')
                    .annotate(count=Count('user')).order_by('-count'))[:3]

    for elem in TOP5Last7Days:
        elem['user'] = Person.objects.get(user_id=elem['user'])

    for elem in TOP3Last30Days:
        elem['user'] = Person.objects.get(user_id=elem['user'])


    context = {
        'TOP5Last7Days': TOP5Last7Days, # Top5 users who have the most repeats in last week
        'TOP3Last30Days': TOP3Last30Days  # Top3 users who have the most treinigs in last month
    }
    return render(request, "./records.html", context)

