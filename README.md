# Django-Chat-App
This project is a small demonstration of a chat app using django.The concept of the app is similar to twilio app, where the concept of rooms exists.Rooms are nothing but a group chat.The user first signs  up, creates a room and then joins it. Once the user joins a room, they can chat with other users in the room.To understand this,one should have good knowledge about `Django` and `Mysql` in depth.

## Prerequisites

- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)

## Installation
- Create a virtual environment
    ```bash
     virtualenv -p python3 foldername
    ```
- Activate the virtual environment
    ```bash
    source bin/activate
    ```
- Install all the dependencies from `requirements.txt`
    ```python
    pip3 install -r requirments.txt
    ```
- Run the flask server
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
- Hit the url `http://localhost:8000/`
