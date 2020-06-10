# core/admin.py

from django.contrib import admin
from .models import Sport  # add this
# Register your models here.

admin.site.register(Sport) # add this