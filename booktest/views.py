from django.shortcuts import render
from booktest.models import *


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')


def editor(request):
    return render(request, 'booktest/editor.html')


def show(request):
    goods = GoodsInfo.objects.get(id=1)
    context = {'g': goods}
    return render(request, 'booktest/show.html', context)
