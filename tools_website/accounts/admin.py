from django.contrib import admin
# Register your models here.
from .models import tools, contactus, nameofuser


admin.site.register(tools)
admin.site.register(contactus)
admin.site.register(nameofuser)
