from django.contrib import admin

# Register your models here.
from .models import Destinations, Blog, UserData, Subscirbe_Emails

admin.site.register(UserData)
admin.site.register(Destinations)
admin.site.register(Blog)
admin.site.register(Subscirbe_Emails)
