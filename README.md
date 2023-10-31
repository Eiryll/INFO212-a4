# Info212-a4

Lab a4 project for Info212.

## Create virtualenv

```powershell
python -m venv venv
```

## Activate virtualenv

```
./venv/Scripts/Activate.ps1
```

## Install libraries

```
pip install -r requirements.txt
```

## Setup database

The project expects a database with the following configuration:

Database name: neo4j
Database username: neo4j
Database password: password1234

(This needs to be setup, if you want to run the project locally)

## Run server

python server.py

## Run seeding

In order to seed the database (create some cars etc.), run:

```
python seed.py
```