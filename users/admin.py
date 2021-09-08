from django.contrib import admin

from .models import User, Biography

# Register your models here.
admin.site.register(User)
admin.site.register(Biography)
