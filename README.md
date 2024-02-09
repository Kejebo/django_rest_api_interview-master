# Interview Task - Enhance REST API

## Goal

We will perform pair programming where you will share your screen and work through the task.

The goal of this task is to evaluate your thought process, design and implementation skills.

You will have about 45 minutes to accomplish as much as you can.

## Task

An API has been built with Django and Django REST Framework.

It current exposes fake salary information for employess via http://127.0.0.1:8000/api/salaries endpoint.

Sqlite is used as the DB backend.

Ensure appropriate HTTP status codes are returned for all responses.

### Question 1

Enhance the `GET` method of `SalariesAPIView` to filter the results by accepting a URL parameter called `name`.

The filtering should allow for partial matches and should be case insensitive.

```
http://127.0.0.1:8000/api/salaries?name=aaron
```

## Question 2

Enhance the API to now also accept new salary information and insert it into the `salaries` table.

The new endpoint should accept a `POST` request. Here is an example:

```
POST http://127.0.0.1:8000/api/salaries

{
    "name": "John Doe",
    "position": "Software Engineer",
    "department": "Engineering",
    "salary": "$5000.00"
}
```

The incoming payload will be serialized to JSON in the `SalariesSerializer` module and then sent to the `SalariesAPIView` for further handling.

## Question 3

Enhance the API to allow a partial update of a single record in the salaries table.

This new endpoint should accept a `PUT` request. Here is an example:

```
PUT http://127.0.0.1:8000/api/salaries/1

{
    "salary": "$100"
}
```
