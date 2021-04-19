from django.contrib import admin
from django.conf import settings
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .utils import register_microservice, register_model


app_models = apps.get_models()
microservice = register_microservice()

for model in app_models:

    register_model(model.__name__, microservice)
    
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass