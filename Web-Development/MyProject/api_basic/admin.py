from calendar import LocaleHTMLCalendar
from django.contrib import admin
from .models import Article, Location,Student


# Register your models here.

admin.site.register(Article)
admin.site.register(Student)
admin.site.register(Location)