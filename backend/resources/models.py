from django.db import models
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
