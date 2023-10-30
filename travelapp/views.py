
from django.http  import HttpResponse
from django.shortcuts import render
from . models import Place, TeamMember

# Create your views here.
def home(request):
    obj=Place.objects.all()
    teamember=TeamMember.objects.all()
    return render(request,"index.html",{'result':obj, 'results':teamember})

def about(request):
    return render (request,"about.html")