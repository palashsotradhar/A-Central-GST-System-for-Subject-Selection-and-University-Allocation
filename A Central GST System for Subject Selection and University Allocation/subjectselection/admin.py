from django.contrib import admin
import inspect
from subjectselection import models

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)
