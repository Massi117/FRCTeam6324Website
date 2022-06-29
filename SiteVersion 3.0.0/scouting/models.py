# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# These are models for scouting data

class EventModel(models.Model):

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length = 100, db_index = True, unique = True)
    date = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name

class ScoutData(models.Model):

    number = models.IntegerField(default=0, blank=True)
    name = models.CharField(max_length=100, db_index = True)
    script = models.CharField(max_length = 100, db_index = True, unique = True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return str(self.number)

class MatchData(models.Model):

    team = models.ForeignKey(ScoutData, related_name='teams', on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel, related_name='events', on_delete=models.CASCADE)

    #Match Data
    habLevelStart = models.IntegerField(default=0, blank=True)
    habLine = models.BooleanField(default=False)
    sandStormCargoAttempts = models.IntegerField(default=0, blank=True)
    sandStormCargoSuccesses = models.IntegerField(default=0, blank=True)
    hatchesPlaced =  models.IntegerField(default=0, blank=True)
    cargoPlaced =  models.IntegerField(default=0, blank=True)
    habLevelEnd = models.IntegerField(default=1, blank =True)
    matchWon = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.team.name