from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import random


pick_res = 'ready to pick'

def picker_template(pick_result='ready to pick'):
    return f'''
    <h1>Random Picker</h1>
    <h2>{pick_result}</h2>
    <h3>separate by line break</h3>
    <form action='/pick/' method='POST'>
        <p><textarea name='lines'></textarea></p>
        <p><input type='submit'></p>
    </form>
    '''


def index(request):
    global pick_res
    return HttpResponse(picker_template(pick_res))


@csrf_exempt
def pick(request: HttpRequest):
    global pick_res
    lines_list = request.POST['lines'].split()
    pick_res = random.choice(lines_list)
    return redirect('/')
