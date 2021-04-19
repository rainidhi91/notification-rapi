from rest_framework.permissions import BasePermission, SAFE_METHODS
import requests
from django.conf import settings


class GlobalViewPermission(BasePermission):

    def has_permission(self, request, view):

        model = view.get_serializer().Meta.model.__name__

        response = None

        parent_class = view.__class__.__bases__[0].__name__

        print(parent_class)

        if request.user.is_authenticated and not request.user.roles:
            url = f"{settings.AUTH_HOST}accounts/permission/{request.user.id}/{parent_class}/{model}/"

        elif not request.user.is_authenticated:
            url = f"{settings.AUTH_HOST}accounts/permission/anonymous/true/{parent_class}/{model}/"

        if request.user.is_authenticated and request.user.roles:
            
            for role in request.user.roles:

                url = f"{settings.AUTH_HOST}accounts/permission/role/{role}/{parent_class}/{model}/"

                response = requests.get(url)

                if response.status_code == 200:
                    response = response.json()
                    break
                else:
                    response = None

        if not response:

            print(url)

            response = requests.get(url)

            if response.status_code == 200:
                response = response.json()
            else:
                response = None

        if not response and not request.user.is_authenticated:
            return False

        elif response:
            if not request.method in response.get("methods"):
                return False

        return True