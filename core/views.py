from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

# Create your views here.

def home(request, color=None):
	polygons = Polygon.objects.all()
	colors = []
	for polygon in polygons:
		if not (polygon.color,polygon.color[1:]) in colors:
			colors+=[(polygon.color,polygon.color[1:])]
	
	if not color is None:
		polygons = Polygon.objects.filter(color__icontains=color)

	return render(request, 'home.html', {'polygons':polygons, 'colors':colors})

def new_map(request):
	if request.method == 'POST':
		form = PolygonForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('/')
