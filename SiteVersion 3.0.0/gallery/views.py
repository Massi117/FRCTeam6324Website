# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import GalleryModel

# Create your views here.

def ImageView(request):

	img = GalleryModel.objects.all()
	args = {'img': img}

	return render(request, 'gallery/viewer.html', args)