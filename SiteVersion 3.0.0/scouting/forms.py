from django import forms
from django.utils.text import slugify
from .models import ScoutData, MatchData

class ScoutForm(forms.ModelForm):

    class Meta:
        model = ScoutData
        fields = (
            'name',
            'number',
        )

        labels = {
            'name': 'Team Name',
            'number': 'Team Number',
        }

    def save(self):
        instance = super(ScoutForm, self).save(commit=False)
        instance.script = slugify(instance.name)
        instance.save()

        return instance

class MatchForm(forms.ModelForm):

    class Meta:
        model = MatchData
        fields = (
            'team',
            'event',
            'habLevelStart',
            'habLine',
            'sandStormCargoAttempts',
            'sandStormCargoSuccesses',
            'hatchesPlaced',
            'cargoPlaced',
            'habLevelEnd',
            'matchWon',
        )

        labels = {
            'team': 'Team #',
            'event': 'Event Name',
            'habLevelStart': 'Starting Level',
            'habLine': 'Did it cross the hab line?',
            'sandStormCargoAttempts': 'Cargo Placement Attempts During Sandstorm',
            'sandStormCargoSuccesses': 'Successful Cargo Placement During Sandstorm',
            'hatchesPlaced': 'The Number of Hatches Placed',
            'cargoPlaced': 'The Number of Cargo Placed',
            'habLevelEnd': 'Ending Level',
            'matchWon': 'Did they win the match?',
        }
