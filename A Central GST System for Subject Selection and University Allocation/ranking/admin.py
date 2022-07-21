from django.contrib import admin
from ranking.models import Subject,Email_Model,Subject_and_University_Model,Subject_and_University_Model2

# Register your models here.
admin.site.register(Subject)
admin.site.register(Email_Model)
admin.site.register(Subject_and_University_Model)
admin.site.register(Subject_and_University_Model2)
