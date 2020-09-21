from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

#def index(request):
#    return render(request, 'index.html')

def profile(request):
    try:
        profile = Profile.objects.get(tag='sw')
        highlights = profile.highlights.all().order_by('-end_date')
        projects = Project.objects.all()
        skills = Skill.objects.all()
    except Profile.DoesNotExist:
        return JsonResponse({"error": "Profile not found."}, status=404)

    return render(request, 'profile.html',{
        'profile' : profile,
        'highlights':highlights,
        'projects':projects,
        'skills':skills,
    })

def skills(request):
    skills = Skill.objects.all()

    # Return skills
    if request.method == "GET":
        return JsonResponse([skill.serialize() for skill in skills], safe=False)

    else:
        return JsonResponse({
            "error": "GET request required."
        }, status=400)