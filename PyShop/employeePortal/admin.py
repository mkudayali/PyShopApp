from django.contrib import admin
from .models import Projects, Employees, Timesheets, Day, TimeSheetMain, TimeSheetDate
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from .forms import TimeSheetMainAdminForm


# Register your models here.


class DaysAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Description')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('ProjectName', 'Description', 'ContactName', 'ContactNumber', 'SpecialNotes')


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('EmpName', 'Designation', 'Mobile', 'StartDate', 'CurrentlyEmployed')


def TimePeriod(obj):
    startdt = DateFormat(obj.StartPeriod)
    enddt = DateFormat(obj.EndPeriod)

    return "%s to %s" % (startdt.format('d/m/Y'), enddt.format('d/m/Y'))

def TotalHours(obj):
    totalHours = obj.Day1 + obj.Day2 + obj.Day3 + obj.Day4 + obj.Day5 + obj.Day6 + obj.Day7
    return totalHours

class TimesheetsAdmin(admin.ModelAdmin):
    list_display = ('EmpUser', TimePeriod, TotalHours)

class ShowPhotoInline(admin.TabularInline):
    model = TimeSheetDate

@admin.register(TimeSheetMain)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('EmpUser','SubmitDate',)
    form = TimeSheetMainAdminForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class TimeSheetDateAdmin(admin.ModelAdmin):
    list_display = ('projectname',)

#admin.site.register(TimeSheetDate,TimeSheetDateAdmin )
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Employees, EmployeesAdmin)
#admin.site.register(Timesheets, TimesheetsAdmin)
#admin.site.register(Day, DaysAdmin)
