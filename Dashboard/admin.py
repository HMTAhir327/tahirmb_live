from django.contrib import admin
from .models import Marage, Relationship,Country,State,City
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Marage)
class MarageAdmin(admin.ModelAdmin):
    list_display = ('age','caste',
    'gender','height','profession','gardian_profession',
    'siblings','married_brothers','married_sisters',
    'marrage_times','referance','referance_person_detail',
    'country',
    'state','city','address','contact','whatsapp')

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','status','updated','created')


class BrandAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Country,BrandAdmin)
admin.site.register(State,BrandAdmin)
admin.site.register(City,BrandAdmin)
