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

E.g.

- `localhost:8000/stats/men_women_decade`
- `localhost:8000/stats/relationship_type_decade`