from django.contrib import admin
from .models import *

admin.site.register(TaskAnnotation)
admin.site.register(Query)
admin.site.register(QueryAnnotation)
admin.site.register(PageLog)
admin.site.register(SERPAnnotation)

