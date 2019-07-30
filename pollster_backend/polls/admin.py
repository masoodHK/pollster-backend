from django.contrib import admin

from .models import Poll, Option, Comments
# Register your models here.
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Comments)