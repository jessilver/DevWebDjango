from django.contrib import admin
from django.apps import apps
from project.settings import MY_APPS

# Evita registrar modelos já registrados
for app_name in MY_APPS:
    models = apps.get_app_config(app_name).get_models()
    for model in models:
        try:
            fields = [field.name for field in model._meta.fields]
            class AutoAdmin(admin.ModelAdmin):
                list_display = fields
            admin.site.register(model, AutoAdmin)
        except admin.sites.AlreadyRegistered:
            pass