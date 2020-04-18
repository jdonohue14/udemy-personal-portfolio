from django.contrib import admin

# Register your models here.
from .models import Blog
# Register your models here.

#added code to get model in the admin page
admin.site.register(Blog)
