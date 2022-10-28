from django.contrib import admin
from .models import Doctors, Doctors_education, Patients, Checkup, Laboratory
from .models import Instrumental, Surgery, Complaint, Gratitude, Accidents


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    exclude = ('doctors_id',)
    list_display = ('full_name', 'sex', 'specialization', 'office')
    list_filter = ('sex', 'specialization', 'office')
    search_fields = ('full_name', 'specialization', 'office')


@admin.register(Doctors_education)
class Doctors_educationAdmin(admin.ModelAdmin):
    exclude = ('doc_educat_id',)
    list_display = ('doc_name', 'education', 'courses', 'degrees')
    list_filter = ('education', 'degrees')
    search_fields = ('doc_name', 'education', 'courses', 'degrees')


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    exclude = ('patients_id',)
    list_display = ('pat_name', 'date_birth', 'sex', 'address')
    list_filter = ('sex',)
    search_fields = ('pat_name',)


@admin.register(Checkup)
class CheckupAdmin(admin.ModelAdmin):
    exclude = ('checkup_id',)
    list_display = ('name_pat', 'name_doc', 'date')
    list_filter = ('date',)
    search_fields = ('name_pat', 'name_doc')


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    exclude = ('laboratory_id',)
    list_display = ('name_pat', 'date', 'type_of_analysis')
    list_filter = ('date', 'type_of_analysis')
    search_fields = ('name_pat',)


@admin.register(Instrumental)
class InstrumentalAdmin(admin.ModelAdmin):
    exclude = ('instrumental_id',)
    list_display = ('name_pat', 'date', 'type_of_research', 'name_doc')
    list_filter = ('date', 'type_of_research')
    search_fields = ('name_pat', 'type_of_research', 'name_doc')


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    exclude = ('surgery_id',)
    list_display = ('name_pat', 'date', 'name_doc', 'name_oper')
    list_filter = ('date',)
    search_fields = ('name_pat', 'name_doc', 'name_oper')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    exclude = ('complaint_id',)
    list_display = ('name_pat', 'date', 'complaint', 'response')
    list_filter = ('date',)
    search_fields = ('name_pat', 'complaint')


@admin.register(Gratitude)
class GratitudeAdmin(admin.ModelAdmin):
    exclude = ('gratitude_id',)
    list_display = ('name_pat', 'date', 'gratitude', 'response')
    list_filter = ('date',)
    search_fields = ('name_pat', 'gratitude')

@admin.register(Accidents)
class AccidentsAdmin(admin.ModelAdmin):
    exclude = ('accidents_id',)
    list_display = ('date','name_doc','name_pat','accident','actions_taken')
    list_filter = ('date',)
    search_fields = ('name_doc','name_pat','accident')