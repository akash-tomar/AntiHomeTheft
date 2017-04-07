# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def getImage(request):
	if request.method == 'POST':
		id_of_user = request.POST.get('id')
		image = request.POST.get('image')

		#send this data to messeneger
