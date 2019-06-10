from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import SafetyLimits

import json

# Create your views here.
def get_limits(request):

	data = [model_to_dict(x) for x in SafetyLimits.objects.all()]

	return render(request, 'jsondump.html', dict(data=json.dumps(data)))