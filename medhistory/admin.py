from django.contrib import admin
from .models import Pet, MedEspeciality, Specie, Veterinarian

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'specie', 'veterinarian', 'age', 'weight',)
    list_filter = ('specie', 'veterinarian',)
    search_fields = ('name', )
    ordering = ('name',)

class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'medespeciality',)
    list_filter = ('medespeciality',)
    search_fields = ('name', )
    ordering = ('name',)

admin.site.register(Pet, PetAdmin)
admin.site.register(MedEspeciality)
admin.site.register(Specie)
admin.site.register(Veterinarian, VeterinarianAdmin)