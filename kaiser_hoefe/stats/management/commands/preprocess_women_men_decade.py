from django.core.management import BaseCommand, CommandError
from django.db import IntegrityError
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from stats.models import Ort
import sqlalchemy
import logging

from stats.models import Person

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Preprocess men and women per decade and save them in own sql table'

    def extract_points(self, df, crs={"init": "epsg:4326"}):
        """
        This functions extracts geometric points from latitude and longitude coordinates
        df: DataFrame with pickup_longitude and pickup_latitude
        crs: Coordinate Reference System
        returns: GeoDataFrame with points as geometry
        """
        geometry = [Point(xy)
                    for xy in zip(df.longitude, df.latitude)]
        df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
        return df

    def sjoin_countries(self, gdf_orte, shapefile):
        """
        This function spatial joins df and nyc_shape
        df: GeoDataFrame with trips and associated Points
        shapefile: Shapefile with all borders from world countries to cities
        returns: GeoDataFrame with all cities and countries
        """

        df_processed = gpd.sjoin(gdf_orte, shapefile)
        return df_processed

    def read_preprocess_orte(self):
        df = pd.DataFrame(list(Ort.objects.all().values()))
        df = df.loc[~df.b.isna() & ~df.l.isna()]
        df.rename({'b':'latitude', 'l':'longitude'}, axis=1, inplace=True)

        return df

    def custom_round(self, x, base=50):
        return int(base * round(float(x) / base))

    def preprocess_persons(self):
        df = pd.DataFrame(list(Person.objects.all().values()))
        df['birthyear'] = df.loc[:, 'f13'].str.slice(0, 4)
        df.birthyear = pd.to_numeric(df.birthyear)
        df = df.loc[~df.birthyear.isna()]
        # Round to next 50 years (custom binning)
        df.birthyear = df.birthyear.apply(lambda x: self.custom_round(x))
        df.birthyear = df.birthyear.astype(int)

        return df


    def preprocess_orte(self):
        shapefile = gpd.read_file('data/countries_shapefile/ne_50m_admin_0_countries.shp')

        print("Preprocess Orte")
        df_orte = self.read_preprocess_orte()

        print("Extract points")
        gdf_orte = self.extract_points(df_orte)

        print("Sjoin countries")
        gdf_joined = self.sjoin_countries(gdf_orte[['ort', 'geometry']], shapefile[['NAME', 'geometry']])
        df_joined = pd.DataFrame(gdf_joined[['ort', 'NAME']])
        df_joined.columns = ['ort', 'land']
        return df_joined

    def handle(self, *args, **options):

        # Read shapefile
        print("Start preprocessing women men")
        df_orte = self.preprocess_orte()
        df_persons = self.preprocess_persons()
        df_merged = \
            pd.merge(df_persons, df_orte, how='left', left_on='f15_id', right_on='ort')
        df_merged.to_csv('data/countries_cities.csv', index=None)







