from django.contrib import admin

from .models import Person,Albums,Musician,Runner,Fruit

admin.site.register(Musician)
admin.site.register(Person)
admin.site.register(Albums)
admin.site.register(Runner)
admin.site.register(Fruit)