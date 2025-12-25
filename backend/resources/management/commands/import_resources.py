import csv
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
