from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

# Create your views here.

def home(request):
	polygons = Polygon.objects.all()
	return render(request, 'home.html', {'polygons':polygons})

def new_map(request):
	if request.method == 'POST':
		form = PolygonForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('/')
