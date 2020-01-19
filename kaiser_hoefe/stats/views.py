import pandas as pd
from django.http import HttpResponse

from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def test(request):
    return HttpResponse("Hello, world. You're at the test.")


def get_women_count(request):
    women_count = Person.objects.filter(f24='w').count()
    return HttpResponse(women_count)


def custom_round(x, base=50):
    return int(base * round(float(x) / base))


def men_women_decade(request):
    """
    Get request which groups all men and women by decade
    :param request:
    :return:
    """
    df = pd.read_csv('data/countries_cities.csv')
    df_grouped = pd.DataFrame(df.groupby(['land', 'f24']).count()['zlabel'])
    df_grouped = pd.DataFrame(df_grouped.to_records())
    df_grouped.columns = ['land', 'geschlecht', 'count']
    return HttpResponse(df_grouped.to_json())
