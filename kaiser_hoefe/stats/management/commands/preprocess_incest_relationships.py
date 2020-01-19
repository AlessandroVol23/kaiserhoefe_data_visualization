from django.core.management import BaseCommand, CommandError
from django.db import IntegrityError
import pandas as pd
from stats.models import Ort, Beziehung, Person


class Command(BaseCommand):
    help = 'Preprocess incest relationships'

    def handle(self, *args, **options):
        df_rel = pd.DataFrame(list(Beziehung.objects.all().values()))
        df_persons = pd.read_csv('data/countries_cities.csv')

        df_parents = df_rel.loc[df_rel.art == 1, ['f41y_id', 'parent']]
        df_parents.columns=['child', 'parent']
        # Get unique parent pair
        df_parents['unique_parent'] = df_parents.groupby('child')['parent'].transform(lambda x: '_'.join(x))

        # Get unique children
        df_parents_un = df_parents.drop_duplicates('child')

        # Get relationship and parents together
        df_rel_parent = pd.merge(df_rel, df_parents_un[['child', 'unique_parent']], how='left', left_on='f41x_id',
                                 right_on='child')

        df_rel_parent.to_csv('data/relationsships_parents.csv', index=None)


