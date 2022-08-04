from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Card)
admin.site.register(Archetype)
admin.site.register(Feature)
admin.site.register(CardFeature)
