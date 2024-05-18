# Contacts app
Contacts application backend using Django Rest Framework

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Pip (Python package installer)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/allanstone/contacts_project.git
    cd contacts_project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the app running.

## Usage

Using the Django Rest Framework you can add contacts, emails, phones, addresses and even social media usernames, if there is an available image it can be used as profile image for the contact

### Example Usage

- To create a new contact, navigate to `http://127.0.0.1:8000/api/contacts/` and fill out the form.
- To fetch for the social media image, fill the desired social media username (only Instagram available by now) and then do this request `http://127.0.0.1:8000/api/contacts/2/profile_image/?platform=instagram` .


http://127.0.0.1:8000/api/contacts/2/profile_image/?platform=instagram

## Features

List the key features of your Django app. For example:

- User authentication and authorization
- Contact post creation and management
- Fetch social media profile images if available

## API Example Request

Here is an example of a web request to your Django app's API:

### Request

```http
GET /api/contacts/2/
Host: example.com
Accept: application/json
```
### Response

```http
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "phones": [
            {
                "id": 3,
                "category": "mobile",
                "number": "+5581181390",
                "contact": 2
            }
        ],
        "emails": [
            {
                "id": 1,
                "email": "alan.garrido.1942@gmail.com",
                "contact": 2
            }
        ],
        "addresses": [
            {
                "id": 1,
                "category": "home",
                "address": "Rio Irapuato 47",
                "contact": 2
            }
        ],
        "first_name": "Alan",
        "last_name": "Garrido Valencia",
        "img_url": "https://i.ibb.co/g98F6g9/e64cfd9b0398.jpg"
    }
]
```
