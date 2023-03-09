from django.contrib import admin
from home.models import Consejos,Aboutus, Banner, Collaborators, Documents, Prueba


@admin.register(Consejos)
class ConsejosAdmin(admin.ModelAdmin):
    list_display = ('name','user','type_consejo')

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Collaborators)
class CollaboratorsAdmin(admin.ModelAdmin):
    list_display = ('name','lastname', 'position')

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title','description','date')

admin.site.register(Banner)

