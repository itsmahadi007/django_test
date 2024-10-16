
create a vitural env with python 3.10
```bash
python3 -m venv venv

# activate the virtual env
source venv/bin/activate
```

install the dependencies
```bash
pip install -r requirements.txt
```

run redis on this port
```bash
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
````

run the server
```bash

# run the server
python manage.py makemigrations
python manage.py migrate

# create a super user
python manage.py createsuperuser

python manage.py runserver

```

to test api

login:
```bash
curl --location 'http://127.0.0.1:8000/api/api-token-auth/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=5T0Ytn4NgWz8lWXBYihAMEY9K0OP4Wcx' \
--data '{
    "username": "admin",
    "password": "1516"
}'
````
author:
```bash
curl --location 'http://127.0.0.1:8000/api/author/' \
--header 'Authorization: token dfd7336dc150908ceb93f6009284991b9b4be6f8' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=5T0Ytn4NgWz8lWXBYihAMEY9K0OP4Wcx' \
--data '{
    "name": "Mahadi Hassan",
    "date_of_birth": "2024-10-16"
}'

```

books:
```bash
curl --location --request GET 'http://127.0.0.1:8000/api/book/' \
--header 'Authorization: token dfd7336dc150908ceb93f6009284991b9b4be6f8' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=5T0Ytn4NgWz8lWXBYihAMEY9K0OP4Wcx' \
--data '{
    "title": "book1",
    "author" : 1,
    "published_date" : "2024-1-5",
    "genre" : "Comic"
}'
```



# run celery worker and beat


```bash

celery -A backend worker --loglevel=info

celery -A backend beat --loglevel=info

```
