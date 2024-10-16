
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

### Base URL
`http://127.0.0.1:8000/api/`


### Authentication
- **Method**: Token Authentication
- **Header**: `Authorization: token <your_access_token>`

### Author Endpoints
Example Curl Request:
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

#### 1. **List Authors**
- **URL**: `/author/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: Retrieve a list of all authors.

#### 2. **Create Author**
- **URL**: `/author/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Data Constraints**:
    ```json
    {
      "name": "[Alphanumeric string]",
      "date_of_birth": "[Date in YYYY-MM-DD format]"
    }
    ```
- **Description**: Add a new author to the system.

#### 3. **Retrieve Author**
- **URL**: `/author/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: Retrieve details of a specific author by ID.

#### 4. **Update Author**
- **URL**: `/author/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Data Constraints**:
    ```json
    {
      "name": "[New name]",
      "date_of_birth": "[New date of birth]"
    }
    ```
- **Description**: Update details of a specific author.

#### 5. **Delete Author**
- **URL**: `/author/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Description**: Remove an author from the system.

### Book Endpoints

Example Curl Request:
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

#### 1. **List Books**
- **URL**: `/book/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: Retrieve a list of all books.

#### 2. **Create Book**
- **URL**: `/book/`
- **Method**: `POST`
- **Auth Required**: Yes
- **Data Constraints**:
    ```json
    {
      "title": "[Book title]",
      "author": "[Author ID]",
      "published_date": "[Date in YYYY-MM-DD format]",
      "genre": "[Genre name]"
    }
    ```
- **Description**: Add a new book to the system.

#### 3. **Retrieve Book**
- **URL**: `/book/{id}/`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: Retrieve details of a specific book by ID.

#### 4. **Update Book**
- **URL**: `/book/{id}/`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Data Constraints**:
    ```json
    {
      "title": "[New title]",
      "author": "[New Author ID]",
      "published_date": "[New published date]",
      "genre": "[New genre]"
    }
    ```
- **Description**: Update details of a specific book.

#### 5. **Delete Book**
- **URL**: `/book/{id}/`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Description**: Remove a book from the system.

---


# run celery worker and beat


```bash

celery -A backend worker --loglevel=info

celery -A backend beat --loglevel=info

```


Please see my profiles:
Mail: mh@mahadihassan.com
GitHub Profile: https://github.com/itsmahadi007
LinkedIn Profile: https://linkedin.com/in/itsmahadi007
Personal Website: https://mahadihassan.com/
Resume: https://www.mahadihassan.com/Mahadi's_Resume.pdf


Open Source: Django Advance Thumbnail Package:
• PyPI: https://pypi.org/project/django-advance-thumbnail/
• GitHub: https://github.com/itsmahadi007/django_advance_thumbnail

