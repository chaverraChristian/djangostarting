"""libreria para la respuesta http"""
from django.http import HttpResponse 
"""modulo de fehca y hora"""
from datetime import datetime
"""libreria para el formato json"""
import json

""" Funcion de prueba para la respuesta http"""
def hello_world (request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello World! Current server time is {now}'.format(now=now))

def hi (request):
    numbers = request.GET['numbers']
    jsonnumbers = json.JSONEncoder().encode({"numbers":[str(numbers)]})
    """print(jsonnumbers)"""
    return HttpResponse(jsonnumbers)