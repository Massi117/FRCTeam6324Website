from django.shortcuts import render, redirect, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ScoutForm, MatchForm
from .models import (ScoutData,
                    MatchData,
                    YearModel,
                    EventModel)

# Create your views here.

def ScoutView(request):
    if request.method =='POST':
        form = ScoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('scouting:scouttable'))
    else:
        form = ScoutForm()

        args = {'form': form}
        return render(request, 'scouting/scoutdata.html', args)


def ScoutTableView(request):

    team = ScoutData.objects.all()
    args = {'team': team}

    return render(request, 'scouting/scouttable.html', args)

'''
ATENTION!!!

This view must change in order to accomadate new game types.

For questions, ask Massi

'''
def ScoutDetailView(request, script=None, *args, **kwargs): 
    
    team = ScoutData.objects.all()
    match = MatchData.objects.all()

    #Must define variables before referencing them
    timeClimb = None
    cubesSwitch = None
    cubesExchange = None
    cubesScale = None
    timeSwitch = None
    timeScale = None
    totalClimb = 0
    obj_autoLine = None
    obj_canClimb = None

    #Makes sure that the pie chart does not recieve a zero as an integer
    def dataIsZero(number):
        if number == 0:
            return 1
        else:
            return float(number)

    #Turns a boolean value to either 0 or 1
    def boolToInt(boolean):
        if boolean == False:
            return 0
        else:
            return 1
    
        
    qs = ScoutData.objects.filter(script__iexact=script.upper())
    if qs.exists() and qs.count() == 1:
        
        obj = qs.first()
                
        obj_init = obj
        obj_name = obj.name
        obj_number = obj.number
        obj_script = obj.script

        #Must define variables before referencing them
        reference = 1
        numberOfMatches = 0
        cubesExchange = 0
        cubesSwitch = 0
        cubesScale = 0
        timeSwitch = 0
        timeClimb = 0
        timeScale = 0
        totalSwitch = 0
        totalExchange = 0
        totalScale = 0
        totalWon = 0
        switchList = []
        scaleList = []
        exchangeList = []
        numberMatch = []

        for matchs in match:
            if matchs.team.name == obj_name:
                totalSwitch += matchs.cubesSwitch
                totalExchange += matchs.cubesExchange
                totalScale += matchs.cubesScale
                totalWon += boolToInt(matchs.matchWon)
                totalClimb += boolToInt(matchs.canClimb)

                cubesSwitch = matchs.cubesSwitch
                cubesExchange = matchs.cubesExchange
                cubesScale = matchs.cubesScale
                cubesSwitch = matchs.cubesSwitch
                cubesExchange = matchs.cubesExchange
                cubesScale = matchs.cubesScale
                obj_autoLine = matchs.autoLine
                obj_canClimb = matchs.canClimb
                timeSwitch += matchs.timeSwitch
                timeClimb += matchs.timeClimb
                timeScale += matchs.timeScale
                numberOfMatches += 1
        
        for matchs in match:
            if matchs.team.name == obj_name:
                switchList.append( matchs.cubesSwitch )
                scaleList.append( matchs.cubesScale )
                exchangeList.append( matchs.cubesExchange )
                numberMatch.append( reference + 1 )



        obj_cubesExchange = float(cubesExchange)
        obj_cubesSwitch = float(cubesSwitch)
        obj_cubesScale = float(cubesScale)
        percentSwitch = float(timeSwitch)/dataIsZero(numberOfMatches)/2.5*100
        percentScale = float(timeScale)/dataIsZero(numberOfMatches)/2.5*100
        percentClimb = float(timeClimb)/dataIsZero(numberOfMatches)/2.5*100
        percentWon = float(totalWon)/dataIsZero(numberOfMatches)
        avSwitch = float(totalSwitch)/dataIsZero(numberOfMatches)
        avScale = float(totalScale)/dataIsZero(numberOfMatches)
        avExchange = float(totalExchange)/dataIsZero(numberOfMatches)


            
    args = {'obj_name': obj_name,
            'obj_number': obj_number,
            'obj_cubesExchange': obj_cubesExchange,
            'obj_cubesSwitch': obj_cubesSwitch,
            'obj_cubesScale': obj_cubesScale,
            'obj_autoLine': obj_autoLine,
            'obj_canClimb': obj_canClimb,
            'obj_script': obj_script,
            'percentClimb': percentClimb,
            'percentScale': percentScale,
            'percentSwitch': percentSwitch,
            'percentWon': percentWon,
            'numberOfMatches': numberOfMatches,
            'numberMatch': numberMatch,
            'switchList': switchList,
            'scaleList': scaleList,
            'exchangeList': exchangeList,
            'avSwitch': avSwitch,
            'avScale': avScale,
            'avExchange': avExchange,
            'team': team,
            'match': match}
                
            
    return render(request, 'scouting/teamdata.html', args)

def ScoutEditView(request, script=None, *args, **kwargs):
    team = ScoutData.objects.all()
    qs = ScoutData.objects.filter(script__iexact=script.upper())

    obj_init = None
    obj_name = None
    if qs.exists() and qs.count() == 1:
        
        obj = qs.first()
        
        obj_init = obj
        obj_name = obj.name


    if request.method == 'POST':
        form = ScoutForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect(reverse('scouting:scouttable'))
    else:
        form = ScoutForm(instance=obj)
        args = {'form': form,
                'obj_name': obj_name,
                'team': team}

        return render(request, 'scouting/scoutedit.html', args)


def MatchAddView(request):
    team = ScoutData.objects.all()

    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('scouting:scouttable'))
    else:
        form = MatchForm()
        args = {'form': form,
                'team': team}

        return render(request, 'scouting/addmatch.html', args)

def YearView(request):
    year = YearModel.objects.all()
    args = {'year': year}
    

    return render(request, 'scouting/years.html', args)

def EventView(request):

    event = EventModel.objects.all()
    args = {'event': event}

    return render(request, 'scouting/events.html', args)
