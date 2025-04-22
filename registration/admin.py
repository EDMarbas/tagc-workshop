# registration/admin.py
from django.contrib import admin
from .models import Registration
import csv # Import the csv module
from django.http import HttpResponse # Import HttpResponse

# Custom Admin Action for CSV Export
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta # Get model metadata
    field_names = [field.name for field in meta.fields] # Get field names

    response = HttpResponse(content_type='text/csv')
    # Suggest a filename for the download
    response['Content-Disposition'] = f'attachment; filename={meta.model_name}_export.csv'
    writer = csv.writer(response)

    writer.writerow(field_names) # Write header row
    for obj in queryset:
        # Write data row for each selected object
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected Registrations as CSV" # Action description


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'location',
        'age_group',
        'current_situation',
        'freelance_experience',
        'registered_at'
    )
    list_filter = (
        'age_group',
        'current_situation',
        'freelance_experience',
        'registered_at',
        'location' # Added location filtering
    )
    search_fields = (
        'full_name',
        'email',
        'location'
    )
    readonly_fields = (
        'registered_at', # Keep registration timestamp read-only
    )
    # Add the custom export action
    actions = [export_as_csv]