from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return HttpResponse('index')

def pick(request, lines):
    lines_list = lines.split(',')
    picked_line = random.choice(lines_list)
    result = f'<h2>{lines}</h2> <h1>{picked_line}</h1>'
    return HttpResponse(result)
