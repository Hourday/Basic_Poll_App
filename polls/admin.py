from django.contrib import admin

from .models import Question
admin.site.register(Question)

from .models import Choice
admin.site.register(Choice)

# Register your models here.

