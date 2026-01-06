from django.contrib import admin
from .models import Admin


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "person":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                user__role__iexact='admin'
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_person_name(self, obj):
            return obj.person.first_name
    
    get_person_name.short_description = 'Nombre'
    
    def get_institution_name(self, obj):
        return obj.institution.name
    
    get_institution_name.short_description = 'Institucion'
    
    
    def delete_admin(modeladmin, request, queryset):
        return queryset.update(is_active=False)
    
    def recover_admin(modeladmin, request, queryset):
        return queryset.update(is_active=True)
    
    list_display = ('id', 'get_person_name', 'get_institution_name', 'is_active')
    list_filter = ('institution__name', 'is_active')
    search_fields = ('person__first_name', 'institution__name')
    actions = [delete_admin, recover_admin]