from django.contrib import admin

from simplereport.models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display=('name','run_link')
admin.site.register(Report, ReportAdmin)