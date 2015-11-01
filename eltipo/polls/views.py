from django.shortcuts import render

# Create your views here.

from polls.models import *

from django.shortcuts import render_to_response

def data(request):
    user = request.user.id
    question = Question.objects.all()
    return render_to_response('index.html',locals())

