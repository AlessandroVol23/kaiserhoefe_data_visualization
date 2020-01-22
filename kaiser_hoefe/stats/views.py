import pandas as pd
from django.http import HttpResponse

from .models import Person, Beziehung, Bild


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
    df_grouped = pd.DataFrame(df.groupby(['birthyear', 'land', 'f24']).count()['zlabel'])
    df_grouped = pd.DataFrame(df_grouped.to_records())
    df_grouped.columns = ['jahr', 'land', 'geschlecht', 'count']
    return HttpResponse(df_grouped.to_json())

def relationship_type_decade(requers):
    df = pd.DataFrame(list(Beziehung.objects.all().values()))
    df_persons = pd.read_csv('data/countries_cities.csv')
    df_joined = pd.merge(df_persons, df, left_on='f41', right_on='f41x_id', how='left')
    df_joined.loc[df_joined.art == 1, 'art'] = 'offspring'
    df_joined.loc[df_joined.art == 2, 'art'] = 'marriage'
    df_grouped = pd.DataFrame(df_joined.groupby(['birthyear', 'land', 'art']).count()['f41'])
    df_grouped = pd.DataFrame(df_grouped.to_records())
    return HttpResponse(df_grouped.to_html())

def incest_relationsships(request):
    df_incest = pd.read_csv('data/incest_relationships.csv')
    return HttpResponse(df_incest.to_json())

def person_birth_death_pic(request):
    df = pd.DataFrame(list(Person.objects.all().values()))
    df['date_of_birth'] = df.f13
    df['date_of_death'] = df.f14
    df['name'] = df.zlabel

    df_bilder = pd.DataFrame(list(Bild.objects.all().values()))
    df_merged = pd.merge(df, df_bilder[['f41_id', 'link']], how='left', left_on='f41', right_on='f41_id')

    df_ret = df_merged[['name', 'date_of_birth', 'date_of_death', 'link']]
    return HttpResponse(df_ret.to_json())