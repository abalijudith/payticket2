from django.contrib import admin

# Register your models here.
from .models import Trip,Agence,Station


admin.site.register(Agence)
admin.site.register(Station)
admin.site.register(Trip)
