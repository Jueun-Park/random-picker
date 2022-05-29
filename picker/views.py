from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import PickRequestSerializers
import random


# TODO: how to delete global variable?
pick_res = 'ready to pick'


@method_decorator(csrf_exempt, name='dispatch')
def random_picker_index(request):
    context = {'pick_res': pick_res}
    return render(request, 'picker/index.html', context)


class PickerView(viewsets.ViewSet):
    serializer_class = PickRequestSerializers

    def pick(self, request: HttpRequest):
        global pick_res
        line_list = request.POST['lines'].split('\n')
        pick_res = random.choice(line_list)
        return redirect('random_picker_index')
