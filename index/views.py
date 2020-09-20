from django.shortcuts import render

# Create your views here.


def index(request):
    template = "index/index.html"
    context = {}
    return render(request, template, context)
