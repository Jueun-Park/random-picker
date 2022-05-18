from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import PickRequestSerializers
import random


# TODO: how to delete global variable?
pick_res = 'ready to pick'


def picker_template(pick_result='ready to pick'):
    return f'''
    <h1>Random Picker</h1>
    <h2>{pick_result}</h2>
    <h3>separate by line break</h3>
    <form action='/picker/' method='POST'>
        <p><textarea name='lines'></textarea></p>
        <p><input type='submit'></p>
    </form>
    '''


class PickerView(viewsets.ViewSet):
    serializer_class = PickRequestSerializers

    def index(self, serializer):
        global pick_res
        return HttpResponse(picker_template(pick_res))

    def pick(self, request: HttpRequest):
        global pick_res
        line_list = request.POST['lines'].split()
        pick_res = random.choice(line_list)
        return redirect('/picker/')
