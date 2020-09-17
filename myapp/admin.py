from django.contrib import admin
from .models import Lead


# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime',)


admin.site.register(Lead, LeadAdmin)
