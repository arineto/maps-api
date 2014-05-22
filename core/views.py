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
	
	if color is not None:
		polygons = Polygon.objects.filter(color__icontains=color)

	return render(request, 'home.html', {'polygons':polygons, 'colors':colors})

def save_map(request, map_id=None):
	if request.method == 'POST':
		if map_id is not None:
			new_points = request.POST.get('points')
			polygon = Polygon.objects.get(id=map_id)
			polygon.points = new_points
			polygon.save()
		else:
			form = PolygonForm(request.POST)
			if form.is_valid():
				form.save()
	return redirect('/')


def delete_map(request, map_id):
	Polygon.objects.get(id=map_id).delete()
	return redirect('/')


def edit_map(request, map_id):
	polygons = Polygon.objects.all()
	colors = []
	for polygon in polygons:
		if not (polygon.color,polygon.color[1:]) in colors:
			colors+=[(polygon.color,polygon.color[1:])]

	return render(request, 'home.html', {'polygons':polygons, 'colors':colors, 'edit':map_id})


