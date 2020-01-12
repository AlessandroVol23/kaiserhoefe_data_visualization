from django.http import HttpResponse
from .models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def test(request):
    return HttpResponse("Hello, world. You're at the test.")

def get_women_count(request):
    women_count = Person.objects.filter(f24 = 'w').count()
    return HttpResponse(women_count)
