from django.shortcuts import render, redirect, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ScoutForm, MatchForm
from .models import (ScoutData,
                    MatchData,
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
    event = EventModel.objects.all()

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
        totalCargo = 0
        totalHatch = 0
        totalsandStormCargoAttempts = 0
        totalsandStormCargoSuccesses = 0
        hatchesPlaced = 0
        cargoPlaced = 0
        totalWon = 0
        numberOfMatches = 0
        habLevelEndList = []
        hatchList = []
        cargoList = []
        numberMatch = []



        for matchs in match:
            if matchs.team.name == obj_name:
                totalHatch += matchs.hatchesPlaced
                totalCargo += matchs.cargoPlaced

                totalWon += boolToInt(matchs.matchWon)
                
                totalsandStormCargoAttempts += matchs.sandStormCargoAttempts
                totalsandStormCargoSuccesses += matchs.sandStormCargoSuccesses
                
                cargoPlaced = matchs.cargoPlaced
                hatchesPlaced = matchs.hatchesPlaced
                obj_autoLine = matchs.habLine
                numberOfMatches += 1

            
        for matchs in match:
            if matchs.team.name == obj_name:
                habLevelEndList.append( matchs.habLevelEnd )
                hatchList.append( matchs.hatchesPlaced)
                cargoList.append( matchs.cargoPlaced )
                numberMatch.append( reference + 1 )



        obj_cargoPlaced = float(cargoPlaced)
        obj_hatchesPlaced = float(hatchesPlaced)

        percentWon = float(totalWon)/dataIsZero(numberOfMatches)
        avHatch = float(totalHatch)/dataIsZero(numberOfMatches)
        avCargo = float(totalCargo)/dataIsZero(numberOfMatches)


            
    args = {# Object Info
            'obj_name': obj_name,
            'obj_number': obj_number,
            'obj_script': obj_script,


            # Averages
            'avHatch': avHatch,
            'avCargo': avCargo,

            # Pie Chart Data
            'percentWon': percentWon,
            'numberOfMatches': numberOfMatches,
            'numberMatch': numberMatch,

            # Line Graph Data
            'cargoList': cargoList,
            'hatchList': hatchList,
            'habLevelEndList': habLevelEndList,

            # Complete Tables
            'team': team,
            'match': match,
            'event': event}
                
            
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



def EventView(request):

    team = ScoutData.objects.all()
    event = EventModel.objects.all()
    args = {'event': event}

    return render(request, 'scouting/events.html', args)

    

def EventDetailView(request, script=None, slug=None, *args, **kwargs):

    team = ScoutData.objects.all()
    match = MatchData.objects.all()
    event = EventModel.objects.all()

    QS = ScoutData.objects.filter(script__iexact=script.upper())
    if QS.exists() and QS.count() == 1:
        objet = QS.first()

        objet_name = objet.name

    qs = EventModel.objects.filter(slug__iexact=slug.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()

        obj_name = obj.name

    args = {'obj_name': obj_name,
            'objet_name': objet_name,
            'team': team,
            'match': match}

    return render(request, 'scouting/eventdetail.html', args)
