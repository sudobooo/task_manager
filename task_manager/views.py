from django.http import HttpResponse
from django.utils.translation import gettext


def hello(request):
    text = gettext('Hello, Hexlet!')
    return HttpResponse(text)
