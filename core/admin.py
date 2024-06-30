from django.contrib import admin

from .models import *

models = [Category, Activity, Entry]

for model in models:
    admin.site.register(model)
