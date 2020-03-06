from django.contrib import admin
from index_page.models import Portfolios
# Register your models here.

class Portfolios_Views(admin.ModelAdmin):
    pass

admin.site.register(Portfolios, Portfolios_Views)