"""
Camden County ReEntry Resources - Seed Data Script
Run: python manage.py shell < seed_camden_data.py
"""

from resources.models import Category, Resource
from django.utils import timezone

# Clear existing data
print("Clearing existing data...")
Resource.objects.all().delete()
Category.objects.all().delete()

# Create categories
print("Creating categories...")
categories = {
    'housing': Category.objects.create(
        name='Housing',
        slug='housing',
        icon_name='home',
        sort_order=1
    ),
    'food': Category.objects.create(
        name='Food Banks',
        slug='food-banks',
        icon_name='food',
        sort_order=2
    ),
    'ids': Category.objects.create(
        name='IDs & Documents',
        slug='ids-docs',
        icon_name='document',
        sort_order=3
    ),
    'health': Category.objects.create(
        name='Health & Clinics',
        slug='health',
        icon_name='health',
        sort_order=4
    ),
    'legal': Category.objects.create(
        name='Legal Aid',
        slug='legal',
        icon_name='legal',
        sort_order=5
    ),
    'employment': Category.objects.create(
        name='Employment',
        slug='employment',
        icon_name='work',
        sort_order=6
    ),
}

# Sample Camden County Resources
resources_data = [
    # HOUSING
    {
        'category': 'housing',
        'name': 'Cathedral Kitchen Homeless Services',
        'address': '601 Market Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9434,
        'longitude': -75.1182,
        'phone': '(856) 365-1000',
        'website': 'https://www.cathedralkitchen.org',
        'description': 'Provides emergency shelter, transitional housing, and supportive services for homeless individuals and families.',
        'hours_of_operation': 'Mon-Sun: 24/7 emergency intake',
        'services_offered': 'Emergency shelter, meals, case management, housing placement',
        'eligibility_notes': 'Open to all experiencing homelessness in Camden County',
    },
    {
        'category': 'housing',
        'name': 'Volunteers of America Delaware Valley',
        'address': '100 S Broad Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9401,
        'longitude': -75.1209,
        'phone': '(856) 541-1819',
        'website': 'https://www.voadv.org',
        'description': 'Transitional housing and reentry support for formerly incarcerated individuals.',
        'hours_of_operation': 'Mon-Fri: 9:00 AM - 5:00 PM',
        'services_offered': 'Transitional housing, employment services, life skills training',
        'eligibility_notes': 'Must be referred by probation/parole or reentry program',
    },
    
    # FOOD BANKS
    {
        'category': 'food',
        'name': 'Cathedral Kitchen Food Pantry',
        'address': '601 Market Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9434,
        'longitude': -75.1182,
        'phone': '(856) 365-1000',
        'website': 'https://www.cathedralkitchen.org',
        'description': 'Hot meals and food pantry services for those in need.',
        'hours_of_operation': 'Breakfast: 7:30 AM, Lunch: 12:00 PM, Dinner: 5:30 PM daily',
        'services_offered': 'Three hot meals daily, food pantry, hygiene products',
        'eligibility_notes': 'No ID required, open to all',
    },
    {
        'category': 'food',
        'name': 'Food Bank of South Jersey',
        'address': '1501 John Tipton Boulevard',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9324,
        'longitude': -75.1243,
        'phone': '(856) 662-4884',
        'website': 'https://www.foodbanksj.org',
        'description': 'Regional food bank providing emergency food assistance.',
        'hours_of_operation': 'Mon-Thu: 8:30 AM - 4:30 PM',
        'services_offered': 'Food boxes, fresh produce, referrals to local pantries',
        'eligibility_notes': 'Proof of Camden County residency',
    },
    {
        'category': 'food',
        'name': 'Joseph\'s House of Camden',
        'address': '1008 Broadway',
        'city': 'Camden',
        'zip_code': '08103',
        'latitude': 39.9489,
        'longitude': -75.1265,
        'phone': '(856) 964-1993',
        'description': 'Emergency food pantry and clothing assistance.',
        'hours_of_operation': 'Mon, Wed, Fri: 10:00 AM - 2:00 PM',
        'services_offered': 'Food bags, clothing, household items',
        'eligibility_notes': 'Walk-ins welcome, once per month',
    },
    
    # IDS & DOCUMENTS
    {
        'category': 'ids',
        'name': 'Camden County MVC Agency',
        'address': '2600 Mt. Ephraim Avenue',
        'city': 'Camden',
        'zip_code': '08104',
        'latitude': 39.9234,
        'longitude': -75.0965,
        'phone': '(609) 292-6500',
        'website': 'https://www.state.nj.us/mvc',
        'description': 'NJ Motor Vehicle Commission for state IDs and driver licenses.',
        'hours_of_operation': 'Mon-Fri: 8:00 AM - 4:30 PM (appointments recommended)',
        'services_offered': 'Non-driver ID, driver license, vehicle registration',
        'eligibility_notes': 'Bring 6 points of ID (birth certificate, Social Security card, etc.)',
    },
    {
        'category': 'ids',
        'name': 'Social Security Administration - Camden',
        'address': '1835 Route 70 East',
        'city': 'Cherry Hill',
        'zip_code': '08003',
        'latitude': 39.9234,
        'longitude': -75.0102,
        'phone': '(800) 772-1213',
        'website': 'https://www.ssa.gov',
        'description': 'Social Security cards, benefits, and replacement documents.',
        'hours_of_operation': 'Mon-Fri: 9:00 AM - 4:00 PM (appointments required)',
        'services_offered': 'Social Security card replacement, benefits application',
        'eligibility_notes': 'Call ahead for required documents',
    },
    
    # HEALTH & CLINICS
    {
        'category': 'health',
        'name': 'CAMcare Health Corporation',
        'address': '800 N. Broad Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9523,
        'longitude': -75.1289,
        'phone': '(856) 342-7500',
        'website': 'https://www.camcare.net',
        'description': 'Federally qualified health center providing primary care and dental services.',
        'hours_of_operation': 'Mon-Fri: 8:00 AM - 8:00 PM, Sat: 9:00 AM - 1:00 PM',
        'services_offered': 'Primary care, dental, behavioral health, pharmacy',
        'eligibility_notes': 'Sliding fee scale, accepts Medicaid/Medicare, uninsured welcome',
    },
    {
        'category': 'health',
        'name': 'Project H.O.P.E. (Health Outreach Prevention Education)',
        'address': '721 Broadway',
        'city': 'Camden',
        'zip_code': '08103',
        'latitude': 39.9445,
        'longitude': -75.1243,
        'phone': '(856) 963-5940',
        'website': 'https://www.hopeworks.org',
        'description': 'HIV/AIDS testing, prevention, and support services.',
        'hours_of_operation': 'Mon-Fri: 9:00 AM - 5:00 PM',
        'services_offered': 'HIV testing, counseling, referrals, syringe exchange',
        'eligibility_notes': 'Free and confidential services',
    },
    {
        'category': 'health',
        'name': 'Osborn Family Health Center',
        'address': '1401 South Broadway',
        'city': 'Camden',
        'zip_code': '08104',
        'latitude': 39.9312,
        'longitude': -75.1187,
        'phone': '(856) 342-3100',
        'website': 'https://www.cooperhealth.org',
        'description': 'Cooper University Health Care community health center.',
        'hours_of_operation': 'Mon-Fri: 8:00 AM - 5:00 PM',
        'services_offered': 'Family medicine, pediatrics, women\'s health, dentistry',
        'eligibility_notes': 'Accepts most insurance, sliding scale available',
    },
    
    # LEGAL AID
    {
        'category': 'legal',
        'name': 'South Jersey Legal Services',
        'address': '745 Market Street, Suite 505',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9456,
        'longitude': -75.1198,
        'phone': '(856) 964-2010',
        'website': 'https://www.lsnj.org',
        'description': 'Free civil legal services for low-income residents.',
        'hours_of_operation': 'Mon-Fri: 8:30 AM - 4:30 PM',
        'services_offered': 'Housing law, family law, consumer law, benefits advocacy',
        'eligibility_notes': 'Must meet income guidelines (at or below 200% poverty level)',
    },
    {
        'category': 'legal',
        'name': 'Camden County Public Defender',
        'address': 'Hall of Justice, 101 S. 5th Street',
        'city': 'Camden',
        'zip_code': '08103',
        'latitude': 39.9412,
        'longitude': -75.1165,
        'phone': '(856) 379-2200',
        'description': 'Legal representation for criminal matters.',
        'hours_of_operation': 'Mon-Fri: 8:30 AM - 4:30 PM',
        'services_offered': 'Criminal defense representation',
        'eligibility_notes': 'Court-appointed for qualifying defendants',
    },
    {
        'category': 'legal',
        'name': 'Rutgers Law School - Criminal & Youth Justice Clinic',
        'address': '217 North Fifth Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9478,
        'longitude': -75.1156,
        'phone': '(856) 225-6078',
        'website': 'https://law.rutgers.edu/clinics',
        'description': 'Free legal help for reentry and expungement matters.',
        'hours_of_operation': 'By appointment only',
        'services_offered': 'Expungement assistance, reentry legal support',
        'eligibility_notes': 'Income-based eligibility',
    },
    
    # EMPLOYMENT
    {
        'category': 'employment',
        'name': 'Camden County One-Stop Career Center',
        'address': '2600 Mt. Ephraim Avenue',
        'city': 'Camden',
        'zip_code': '08104',
        'latitude': 39.9234,
        'longitude': -75.0965,
        'phone': '(856) 964-8950',
        'website': 'https://www.camdencounty.com/service/employment',
        'description': 'Job search assistance, training programs, and career counseling.',
        'hours_of_operation': 'Mon-Fri: 8:30 AM - 4:30 PM',
        'services_offered': 'Job search, resume help, skills training, computer access',
        'eligibility_notes': 'Open to all job seekers, no ID required for basic services',
    },
    {
        'category': 'employment',
        'name': 'Hopeworks Camden',
        'address': '300 Market Street',
        'city': 'Camden',
        'zip_code': '08102',
        'latitude': 39.9423,
        'longitude': -75.1156,
        'phone': '(856) 382-7784',
        'website': 'https://www.hopeworks.org',
        'description': 'Youth job training in technology and GIS mapping.',
        'hours_of_operation': 'Mon-Fri: 9:00 AM - 5:00 PM',
        'services_offered': 'Tech training, paid internships, job placement',
        'eligibility_notes': 'Ages 18-26, Camden residents',
    },
    {
        'category': 'employment',
        'name': 'Center for Family Services - Reentry Program',
        'address': '2101 N. Haddon Avenue',
        'city': 'Camden',
        'zip_code': '08103',
        'latitude': 39.9567,
        'longitude': -75.1078,
        'phone': '(856) 964-1990',
        'website': 'https://www.centerffs.org',
        'description': 'Employment services specifically for formerly incarcerated individuals.',
        'hours_of_operation': 'Mon-Fri: 9:00 AM - 5:00 PM',
        'services_offered': 'Job readiness, employment placement, mentoring',
        'eligibility_notes': 'Must be referred by probation or reentry program',
    },
]

# Create resources
print("Creating resources...")
for data in resources_data:
    category_key = data.pop('category')
    Resource.objects.create(
        category=categories[category_key],
        last_verified_date=timezone.now().date(),
        source='Manual Entry - MVP Seed Data',
        active=True,
        **data
    )
    print(f"  ✓ {data['name']}")

print(f"\n Created {Category.objects.count()} categories")
print(f" Created {Resource.objects.count()} resources")
print("\nYou can now:")
print("  1. Visit http://localhost:8000/admin to manage resources")
print("  2. Visit http://localhost:8000/api/resources/ to see the API")
print("  3. Start the React frontend to see the full app")
