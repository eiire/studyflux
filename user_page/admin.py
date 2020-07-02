from django.contrib import admin
from user_page.models import Knowledge
# Register your models here.


class KnowledgeViews(admin.ModelAdmin):
    pass


admin.site.register(Knowledge, KnowledgeViews)