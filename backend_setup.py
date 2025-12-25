#!/usr/bin/env python3
"""
ReEntry Compass - Backend Setup Script
Generates complete Django project structure
Run: python3 this_script.py
"""

import os
import sys

def create_file(path, content):
    """Create file with content, making dirs as needed"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✓ Created {path}")

def main():
    print("Creating ReEntry Compass Backend...\n")
    
    # Project structure
    BASE = "backend"
    
    # ============ requirements.txt ============
    create_file(f"{BASE}/requirements.txt", """Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
""")
    
    # ============ manage.py ============
    create_file(f"{BASE}/manage.py", """#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reentry_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
""")
    
    # ============ settings.py ============
    create_file(f"{BASE}/reentry_api/settings.py", """import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this-in-production-12345')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reentry_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'reentry_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings - allow frontend dev server
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
if not DEBUG:
    CORS_ALLOWED_ORIGINS = [os.getenv('FRONTEND_URL', '')]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': None,  # Return all resources
}
""")
    
    # ============ urls.py (main) ============
    create_file(f"{BASE}/reentry_api/urls.py", """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('resources.urls')),
]
""")
    
    # ============ wsgi.py ============
    create_file(f"{BASE}/reentry_api/wsgi.py", """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reentry_api.settings')
application = get_wsgi_application()
""")
    
    # ============ __init__.py files ============
    create_file(f"{BASE}/reentry_api/__init__.py", "")
    create_file(f"{BASE}/resources/__init__.py", "")
    
    # ============ models.py ============
    create_file(f"{BASE}/resources/models.py", """from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    icon_name = models.CharField(max_length=50, blank=True)
    sort_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name

class Resource(models.Model):
    # Basic info
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources')
    
    # Location
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default='NJ')
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    
    # Contact
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    # Details
    description = models.TextField(blank=True)
    hours_of_operation = models.TextField(blank=True)
    eligibility_notes = models.TextField(blank=True)
    services_offered = models.TextField(blank=True)
    
    # Verification
    active = models.BooleanField(default=True)
    last_verified_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=255, blank=True)
    admin_notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"

class IssueReport(models.Model):
    ISSUE_TYPES = [
        ('wrong_address', 'Wrong Address'),
        ('wrong_hours', 'Wrong Hours'),
        ('closed', 'Permanently Closed'),
        ('wrong_phone', 'Wrong Phone Number'),
        ('other', 'Other'),
    ]
    
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='issue_reports')
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    description = models.TextField()
    reporter_contact = models.CharField(max_length=255, blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.resource.name} - {self.issue_type}"
""")
    
    # ============ serializers.py ============
    create_file(f"{BASE}/resources/serializers.py", """from rest_framework import serializers
from .models import Resource, Category, IssueReport

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon_name']

class ResourceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Resource
        fields = [
            'id', 'name', 'category', 'address', 'city', 'state', 'zip_code',
            'latitude', 'longitude', 'phone', 'website', 'email',
            'description', 'hours_of_operation', 'eligibility_notes',
            'services_offered', 'last_verified_date'
        ]

class IssueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueReport
        fields = ['resource', 'issue_type', 'description', 'reporter_contact']
""")
    
    # ============ views.py ============
    create_file(f"{BASE}/resources/views.py", """from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Resource, Category, IssueReport
from .serializers import ResourceSerializer, CategorySerializer, IssueReportSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ResourceSerializer
    
    def get_queryset(self):
        queryset = Resource.objects.filter(active=True)
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

@api_view(['POST'])
def report_issue(request):
    serializer = IssueReportSerializer(data=request.data)
    if serializer.is_valid():
        issue = serializer.save()
        
        # Send email notification (configure email in production)
        try:
            resource = issue.resource
            send_mail(
                f'Resource Issue Report: {resource.name}',
                f'''
Issue Type: {issue.get_issue_type_display()}
Resource: {resource.name}
Address: {resource.address}
Description: {issue.description}
Reporter Contact: {issue.reporter_contact or "Not provided"}

View in admin: /admin/resources/issuereport/{issue.id}/
                ''',
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMINS[0][1]] if settings.ADMINS else [],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email send failed: {e}")
        
        return Response({
            'success': True,
            'message': 'Report submitted successfully'
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
""")
    
    # ============ urls.py (app) ============
    create_file(f"{BASE}/resources/urls.py", """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'resources', views.ResourceViewSet, basename='resource')

urlpatterns = [
    path('', include(router.urls)),
    path('report-issue/', views.report_issue, name='report-issue'),
]
""")
    
    # ============ admin.py ============
    create_file(f"{BASE}/resources/admin.py", """from django.contrib import admin
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
""")
    
    # ============ Management command: import_resources ============
    create_file(f"{BASE}/resources/management/__init__.py", "")
    create_file(f"{BASE}/resources/management/commands/__init__.py", "")
    create_file(f"{BASE}/resources/management/commands/import_resources.py", """import csv
from django.core.management.base import BaseCommand
from resources.models import Resource, Category

class Command(BaseCommand):
    help = 'Import resources from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            created = 0
            updated = 0
            
            for row in reader:
                # Get or create category
                category_name = row.get('category', 'Other')
                category, _ = Category.objects.get_or_create(
                    name=category_name,
                    defaults={'slug': category_name.lower().replace(' ', '-')}
                )
                
                # Create or update resource
                resource, is_new = Resource.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'category': category,
                        'address': row.get('address', ''),
                        'city': row.get('city', ''),
                        'state': row.get('state', 'NJ'),
                        'zip_code': row.get('zip_code', ''),
                        'latitude': row.get('latitude') or None,
                        'longitude': row.get('longitude') or None,
                        'phone': row.get('phone', ''),
                        'website': row.get('website', ''),
                        'email': row.get('email', ''),
                        'description': row.get('description', ''),
                        'hours_of_operation': row.get('hours_of_operation', ''),
                        'eligibility_notes': row.get('eligibility_notes', ''),
                        'services_offered': row.get('services_offered', ''),
                        'source': row.get('source', 'CSV Import'),
                        'active': True,
                    }
                )
                
                if is_new:
                    created += 1
                else:
                    updated += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Import complete: {created} created, {updated} updated'
            )
        )
""")
    
    # ============ .env.example ============
    create_file(f"{BASE}/.env.example", """SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
FRONTEND_URL=http://localhost:5173

# Email settings (for issue reports)
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
# DEFAULT_FROM_EMAIL=noreply@reentrycompass.org
""")
    
    # ============ .gitignore ============
    create_file(f"{BASE}/.gitignore", """*.pyc
__pycache__/
db.sqlite3
.env
staticfiles/
venv/
.DS_Store
""")
    
    print(f"\n Backend structure created in '{BASE}/' directory")
    print("\nNext steps:")
    print("1. cd backend")
    print("2. python3 -m venv venv")
    print("3. source venv/bin/activate")
    print("4. pip install -r requirements.txt")
    print("5. python manage.py migrate")
    print("6. python manage.py createsuperuser")
    print("7. python manage.py runserver")

if __name__ == '__main__':
    main()
