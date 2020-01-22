import pandas as pd
from django.core.management import BaseCommand
from stats.models import Beziehung


class Command(BaseCommand):
    help = 'Preprocess incest relationships'

    def preprocess_unique_parents(self):
        df_rel = pd.DataFrame(list(Beziehung.objects.all().values()))
        df_persons = pd.read_csv('data/countries_cities.csv')

        df_parents = df_rel.loc[df_rel.art == 1, ['f41y_id', 'f41x_id']]
        df_parents.columns = ['child', 'parent']
        df_parents.parent = df_parents.parent.astype(str)
        # Get unique parent pair
        df_parents['unique_parent'] = df_parents.groupby('child')['parent'].transform(lambda x: '_'.join(x))

        # Get unique children
        df_parents_un = df_parents.drop_duplicates('child')

        # Get relationship and parents together
        df_rel_parent = pd.merge(df_rel, df_parents_un[['child', 'unique_parent']], how='left', left_on='f41x_id',
                                 right_on='child')
        return df_rel_parent

    def handle(self, *args, **options):
        # Get all Children with unique parent pairs
        df_rel_parent = self.preprocess_unique_parents()

        # Get just marriages
        df_marriages = df_rel_parent.loc[df_rel_parent.art == 2]

        # Get all Persons
        df_persons = pd.read_csv('data/countries_cities.csv')

        # Merge birthyear to children and parents
        df_merged = pd.merge(df_marriages, df_persons[['f41', 'birthyear', 'land']], how='left', left_on='f41x_id',
                             right_on='f41')

        # First count how many marriages have the same parrent
        df_incest = pd.DataFrame(df_merged.groupby('unique_parent').count()['art'])
        df_incest.reset_index(inplace=True)
        df_incest.columns = ['unique_parent', 'count_incest']

        # Merge incest to merged to have year and country
        df_incest_year_country = pd.merge(df_merged, df_incest, how='left', left_on='unique_parent',
                                          right_on='unique_parent')

        df_incest_year_country_grouped = df_incest_year_country.groupby(['birthyear', 'land']).agg({
            'count_incest': 'sum'
        })

        # Remove multi index
        df_incest_year_country_grouped = pd.DataFrame(df_incest_year_country_grouped.to_records())

        # Then sum up and aggregate by country and year

        df_incest_year_country_grouped.columns = ['jahr', 'land', 'count_incest']

        df_incest_year_country_grouped.to_csv('data/incest_relationships.csv', index=None)
