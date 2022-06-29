from django import forms
from django.utils.text import slugify
from .models import ScoutData, MatchData

class ScoutForm(forms.ModelForm):

    class Meta:
        model = ScoutData
        fields = (
            'name',
            'number',
            'autoLine',
            'autoSwitch',
            'autoScale',
            'climb',
            'scale',
            'switch',
        )

        labels = {
            'name': 'Team Name',
            'number': 'Team Number',
            'autoLine': 'Can cross auto line?',
            'autoSwitch': 'Can place a cube on switch during autonomous?',
            'autoScale': 'Can place a cube on scale during autonomous?',
            'climb': 'Can climb?',
            'scale': 'Can place a cube on scale?',
            'switch': 'Can place a cube on switch?',
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
            'autoLine',
            'cubesSwitch',
            'cubesExchange',
            'cubesScale',
            'canClimb',
            'timeCube',
            'timeClimb',
            'timeSwitch',
            'timeScale',
            'matchWon',
        )

        labels = {
            'autoLine': 'Crossed auto line?',
            'cubesSwitch': 'How many cubes were placed on the switch?',
            'cubesExchange': 'How many cubes were placed in the exchange?',
            'cubesScale': 'How many cubes were placed on the scale?',
            'canClimb': 'Did the robot climb?',
            'timeCube': 'About how much time did the robot spend on the exchange? (In minutes)',
            'timeClimb': 'About how much time did the robot spend climbing? (In minutes)',
            'timeSwitch': 'About how much time did the robot spend on the switches? (In minutes)',
            'timeScale': 'About how much time did the robot spend on the scale? (In minutes)',
            'matchWon': 'Did they win the match?',
        }
