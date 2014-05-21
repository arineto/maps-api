from django.forms import ModelForm
from core.models import *

class PolygonForm(ModelForm):

	class Meta:
		model = Polygon