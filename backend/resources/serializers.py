from rest_framework import serializers
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
