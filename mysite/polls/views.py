from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! You are at the polls index!")


def luke(request):
    return HttpResponse("Hello, dear Luke")


def arthur(request):
    return HttpResponse("Hello, dear Arthur")
