from django.contrib import admin

# Register your models here.(add model to admin)
from .models import Post ## (add model to admin)
admin.site.register(Post) ## (add model to admin)