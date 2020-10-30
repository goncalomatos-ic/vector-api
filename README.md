# Vector API

This is Python3.8 + [Starlette](https://www.starlette.io/) api, running on a [Uvicorn](https://www.uvicorn.org/) ASGI server.
The SQL Toolkit for this api is PostgreSQL, which is managed by [SQLAlchemy](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## Install

1. Install [Python3](https://www.python.org/downloads/)

2. Install Starlette + Uvicorn
```
$ pip3 install starlette

$ pip3 install uvicorn
```

Starlette is not strictly tied to any particular database implementation.
Starlette's databases package provides SQLAlchemy core support against a range of different database drivers.

3. Install Alembic 

```
$ pip3 install alembic
```

## Run
The server will be running on `localhost:8000` (default)

```
uvicorn app.main:app
```

## Migrations

### Create 
```
alembic revision -m "Create X table"
```

### Migrate
```
alembic upgrade head
```

## Build

### Freeze dependencies
```
pip freeze > requirements.txt
```

### Install dependencies

```pip install -r requirements.txt```
