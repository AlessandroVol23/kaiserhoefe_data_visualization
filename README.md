# Kaiser Hoefe Data Visualization

## Docker

All docker services are combined in `docker_compose.yml`. You can start them with the command 
`docker_compose up`. 

## Data

The data is hosted on a mysql database within a docker container.

You can access the data then with any DBS on `localhost:1234`.

- User: infoviz
- Password: kaiserhoefe

## Django

Django will also be started in the docker container and uses the MySQL database as backend.
You can access Django on the url: `localhost:8000`. 
On `localhost:8000/admin` you can access the admin page, currently with:
- User: admin
- Password: password

## API

There are several GET requests available. All URLs can be seen in `kaiser_hoefe/stats/urls.py` and the views 
in `kaiser_hoefe/stats/views.py`.

GET requests are:

- `localhost:8000/stats/men_women_decade`
   - Shows all people aggregated by country, year (in 50 steps) and gender

__Response__
```json
{
  "jahr": {
    "0": 1100,
    "1": 1100,
    "2": 1150,
    "3": 1150,
  },
  "land": {
    "0": "Czechia",
    "1": "Germany",
    "2": "Czechia",
    "3": "Germany",
  },
  "geschlecht": {
    "0": "m",
    "1": "m",
    "2": "m",
    "3": "m",
  },
  "count": {
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 1,
  }
}
```

- `localhost:8000/stats/relationship_type_decade`
    - Shows all incest relationships per country, year (50s)
    
__Response__
```json
{
  "jahr": {
    "0": 1200,
    "1": 1300,
    "2": 1300,
    "3": 1350
  },
  "land": {
    "0": "France",
    "1": "Austria",
    "2": "Germany",
    "3": "Austria"
  },
  "count_incest": {
    "0": 1,
    "1": 2,
    "2": 1,
    "3": 2
  }
}
```

- `localhost:8000/stats/person_birth_death_pic`
    - Shows all people with name, date of birth, date of death and link to picture
    
__Response__
```json
{
  "name": {
    "0": "Habsburg, Ferdinand III. (1608–1657), Kaiser des Heiligen Römischen Reiches",
    "1": "Thun, Christoph Simon (1582–1635), Großprior des Malteserordens in Ungarn",
    "2": "Trauttmansdorff, Maximilian (1584–1650), Obersthofmeister",
    "3": "Auersperg, Johann Weikhard (1615–1677), Obersthofmeister"
  },
  "date_of_birth": {
    "0": "1608 Jul 13",
    "1": "1582 Sep 12",
    "2": "1584 Mai 23",
    "3": "1615 Mar 11"
  },
  "date_of_death": {
    "0": "1657 Apr 02",
    "1": "1635 Mar 27",
    "2": "1650 Jun 08",
    "3": "1677 Nov 13"
  },
  "link": {
    "0": "http://commons.wikimedia.org/wiki/File:Ferdinand_III,_Holy_Roman_Emperor.jpg",
    "1": "",
    "2": "http://commons.wikimedia.org/wiki/File:Anselmus-van-Hulle-Hommes-illustres_MG_0465.tif",
    "3": ""
  }
}
```