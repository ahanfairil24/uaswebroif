from django.contrib import admin

from .models import santri

class santriAdmin(admin.ModelAdmin):
    pass
admin.site.register(santri, santriAdmin)


# Register your models here.
