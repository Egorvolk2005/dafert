from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profiles





admin.site.register(Profiles, UserAdmin)
