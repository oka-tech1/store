from django.contrib import admin
# Register your models here.
from .models import tools, contactus, profile, order_emails


admin.site.register(tools)
admin.site.register(contactus)
admin.site.register(profile)
admin.site.register(order_emails)	
