"""libreria para la respuesta http"""
from django.http import HttpResponse 
"""modulo de fehca y hora"""
from datetime import datetime
"""libreria para el formato json"""
import json

""" Funcion de prueba para la respuesta http"""
def hello_world (request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(
        'Hello World! Current server time is {now}'.format(now=now))

def sort_numbers (request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type = 'application/json')


def say_hi (request, name, age):
    if age < 12:
        message = '{}, U are not allowed here'.format(name)
    else:
        message = 'Hello {}! Welcome'.format(name)
    return HttpResponse(message)