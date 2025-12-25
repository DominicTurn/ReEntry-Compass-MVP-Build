from rest_framework import viewsets, status
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
