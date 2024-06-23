from django.contrib import admin

from .models import *

models = [Activity, Entry, ActivityEntry]

for model in models:
    admin.site.register(model)
