from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def categoryPost(self, input):
    return HttpResponse("testing {}".format(input))
