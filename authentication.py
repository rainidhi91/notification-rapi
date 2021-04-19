from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
import requests


class CustomUser:
    is_authenticated = True

    def __init__(self, id, roles, email, company, is_authenticated):
        self.id = id
        self.roles = roles
        self.email = email
        self.company = company
        self.company = company
        self.is_authenticated = is_authenticated
    
    def __str__(self):
        return self.email


class APIAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        response = {}

        if token:
            url = settings.AUTH_HOST + "accounts/"
            response = requests.get(url, headers = {"Authorization": token})
            
            if response.status_code == 200:
                
                response = response.json()

                if response["company"]:
                    url = settings.CRM_HOST + f"company/{response['company']}/edit/"

                    response2 = requests.get(url)
                    
                    if response2.status_code == 200:
                        response["company"] = response2.json()
                    else:
                        response["company"] = ""

            else:
                response = {}


        user = CustomUser(
            id = response.get("id", None),
            roles = response.get("roles", []),
            email = response.get("email"),
            company = response.get("company"),
            is_authenticated = bool(response),
        )

        return (user, True) # authentication successful
