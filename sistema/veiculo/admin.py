from django.contrib import admin
from django.apps import apps
from project.settings import MY_APPS

for app_name in MY_APPS:
    models = apps.get_app_config(app_name).get_models()
    for model in models:
        admin.site.register(model)