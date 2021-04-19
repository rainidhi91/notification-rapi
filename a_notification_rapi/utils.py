import requests
from django.conf import settings


def get_all_users():
    users = []

    url = f"{ settings.AUTH_HOST }accounts/register/"

    response  = requests.get(url)

    if response.status_code == 200:
        users = map(lambda x: (x["id"], x["email"]), response.json())

    return tuple(users)


def get_all_roles():
    roles = []

    url = f"{ settings.AUTH_HOST }accounts/roles/"

    response  = requests.get(url)

    if response.status_code == 200:
        roles = map(lambda x: (x["name"], x["name"]), response.json())

    return tuple(roles)


def register_microservice():

    output = {}

    url = f"{ settings.AUTH_HOST }accounts/microservice/{settings.MS_NAME}/"

    response = requests.get(url)

    if response.status_code == 200:
        output = response.json()
    else:

        url = f"{ settings.AUTH_HOST }accounts/microservice/"

        data = {
            "name" : settings.MS_NAME,
        }

        response = requests.post(url, data = data)

        if response.status_code == 201:
            output = response.json()

    return output


def register_model(model_name, microservice):

    url = f"{ settings.AUTH_HOST }accounts/model/"

    requests.post(url, data = {
        "name" : model_name,
        "microservice" : microservice.get("id"),
    })