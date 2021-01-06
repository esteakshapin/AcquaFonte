# Acqua Fonte

Crowd sourced water fountian locator.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python
Node npx
GEOS 
PROJ.4 
GDAL
Docker
```

### Installing backend (django)

Need to set up a python virtual env with the required packages. first cd into the project backend directory

setup virtual enviroment
```
cd backend
python3 -m venv venv
source venv/bin/activate
```

instlal required python libraries. Cd into src directory.

```
cd src
pip isntall -r requirements.txt
```

install the required geo packages for geodjango. Steps listed for linux based system

```
sudo apt install gdal-bin libgdal-dev
sudo apt install python3-gdal
sudo apt install binutils libproj-dev
```

set up PostgreSQL and PostGIS database

```
docker volume create gis_data # creating colume to save date; Persist Data
docker run --name=postgis -d -e POSTGRES_USER=GIS_DATABASE_USERNAME -e POSTGRES_PASS=GIS_DATABASE_PASSWORD -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v gis_data:/var/lib/postgresql --restart=always kartoza/postgis:9.6-2.4
```
GIS_DATABASE_USERNAME and GIS_DATABASE_PASSWORD can be anything you want. The valiables should be set in the env file.

Check https://realpython.com/location-based-app-with-geodjango-tutorial/ for more info on how to set up geodjango

### Set up enviroment variables
```
touch .env
nano .env

# set up variable values
GEOCODE_API_KEY = 
GIS_DATABASE_USERNAME = 
GIS_DATABASE_PASSWORD = 
SECRET_KEY = 
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc