from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Resource, IssueReport

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'sort_order']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'city', 'active', 'last_verified_date', 'phone']
    list_filter = ['category', 'active', 'city']
    search_fields = ['name', 'address', 'description', 'services_offered']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'active')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code', 'latitude', 'longitude')
        }),
        ('Contact', {
            'fields': ('phone', 'website', 'email')
        }),
        ('Details', {
            'fields': ('description', 'hours_of_operation', 'eligibility_notes', 'services_offered')
        }),
        ('Verification', {
            'fields': ('last_verified_date', 'source', 'admin_notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_verified_today', 'mark_inactive']
    
    def mark_verified_today(self, request, queryset):
        from django.utils import timezone
        queryset.update(last_verified_date=timezone.now().date())
    mark_verified_today.short_description = "Mark as verified today"
    
    def mark_inactive(self, request, queryset):
        queryset.update(active=False)
    mark_inactive.short_description = "Mark as inactive"

@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display = ['resource', 'issue_type', 'resolved', 'created_at', 'reporter_contact']
    list_filter = ['issue_type', 'resolved', 'created_at']
    search_fields = ['resource__name', 'description']
    readonly_fields = ['created_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('resource')
