from django.contrib import admin
#added libraries
from .models import Project
# Register your models here.

#added code to get model in the admin page
admin.site.register(Project)
