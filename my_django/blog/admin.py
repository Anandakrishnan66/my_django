from django.contrib import admin

# Register your models here.
from .models import Blog,Entry,Author,Authors,Book,Store,Publisher

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Authors)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Entry)