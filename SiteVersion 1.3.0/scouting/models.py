# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# These are models for scouting data

class YearModel(models.Model):

    year = models.CharField(max_length=100, blank=False)
    game = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.year

class EventModel(models.Model):

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length = 100, db_index = True, unique = True)
    date = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    year = models.ForeignKey(YearModel, related_name='years')


    def __str__(self):
        return self.name

class ScoutData(models.Model):

    number = models.IntegerField(default=0, blank=True)
    name = models.CharField(max_length=100, db_index = True)
    script = models.CharField(max_length = 100, db_index = True, unique = True)
    #event = models.ForeignKey(EventModel, related_name='events')

    #Team Abilities
    autoLine = models.BooleanField(default=False)
    autoScale = models.BooleanField(default=False)
    autoSwitch = models.BooleanField(default=False)
    climb = models.BooleanField(default=False)
    scale = models.BooleanField(default=False)
    switch = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return str(self.number)

class MatchData(models.Model):

    team = models.ForeignKey(ScoutData, related_name='teams')
    #event = models.ForeignKey(EventModel, related_name='events')

    #Match Data
    autoLine = models.BooleanField(default=False)
    cubesSwitch = models.IntegerField(default=0, blank=True)
    cubesExchange = models.IntegerField(default=0, blank=True)
    cubesScale = models.IntegerField(default=0, blank=True)
    canClimb = models.BooleanField(default=False)
    refNumber = models.IntegerField(default=1, blank=False)
    timeCube = models.FloatField(default=0, blank=False)
    timeClimb = models.FloatField(default=0, blank=False)
    timeSwitch = models.FloatField(default=0, blank=False)
    timeScale = models.FloatField(default=0, blank=False)
    matchWon = models.BooleanField(default=False)
    autoScale = models.BooleanField(default=False)
    autoSwitch = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Match Data'
        verbose_name_plural = 'Match Data'

    def __str__(self):
        return self.team.name
