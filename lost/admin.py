from django.contrib import admin
from lost.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_object', 'created_by', 'status', 'posted_at')
    list_filter = ('status', 'posted_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'type_of_object', 'description')
        }),
        ('Location Details', {
            'fields': ('location_found', 'pickup_details')
        }),
        ('User Details', {
            'fields': ('created_by', 'posted_at')
        }),
        ('Availability', {
            'fields': ('status', 'image')
        }),
    )
