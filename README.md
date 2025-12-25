# ReEntry-Compass-MVP-Build
A secure, self-hosted backend that powers the ReEntry Compass platform. A reentry-focused SaaS designed to help returning citizens access documents, housing, mental health, employment resources, and more.


Purpose of This Project


ReEntry Compass aims to become a full SaaS platform for:


    • Returning citizens
    • 
    • Case managers
    • 
    • Reentry programs
    • 
    • Nonprofits
    • 
    • County agencies
      

This backend currently supports:


Document Vault (upload & store client documents)

Resource Directory (housing, employment, mental health, and other services)

Admin Dashboard (secure management for resources and documents)

This is the foundation of a long-term, scalable SaaS platform.


Technologies Used


    • Python 3.12
    • Django 5.x
    • Django REST Framework
    • Django CORS Headers
    • SQLite (temporary) → will migrate to PostgreSQL later
    • Gunicorn + Nginx (future production stack)
    • Ubuntu VPS on public IP



    Features Completed (MVP 0.1)
1. Backend skeleton
    • Django project initialized
    • Virtual environment created
    • Required libraries installed
    • CORS + DRF enabled
2. Document Model
Stores uploaded files for returning citizens:
    • Title
    • Category
    • File
    • Associated User (optional for now)
    • Timestamp
3. Resource Model
Directory of reentry-friendly services:
    • Name
    • Category (Housing, Mental Health, Employment, etc.)
    • Description
    • Address / City / State / ZIP
    • Website
    • Phone
    • Accepts Felony (True/False)
4. Admin Dashboard
    • Superuser account created
    • Models registered in admin
    • Full CRUD on Documents & Resources
5. Media File Handling
    • /media/ folder created
    • File upload paths configured
    • Static media served in dev mode
6. Server Running Publicly
    • File upload paths configured
    • Static media served in dev mode
   
7. Server Running Publicly



What’s Next (Roadmap)

     (User System)
    • Custom user model
    • Roles: Client / Case Manager / Admin
    • Authentication (JWT or Session Auth)
      (API Layer)
    • REST endpoints for Resources
    • REST endpoints for Documents
    • Upload via API

    • Client registration
    • Case manager dashboard
    • Multi-tenant architecture
    • PostgreSQL migration
    • Full deployment with Nginx + Gunicorn
    • HTTPS + real domain (reentrycompass.com)

Founder Background

I began this project after coming home from 11 years of incarceration and experiencing just how confusing and difficult the reentry process can be. The uncertainty, the lack of guidance, and the challenge of rebuilding from nothing.


With a growing background in cybersecurity and software development, I’m building ReEntry Compass to give returning citizens the tools I wish I had access to: secure document storage, reliable resources, and real support.
It’s designed with security at the core and built to evolve into a scalable SaaS platform that can support individuals, case managers, and county reentry programs nationwide.


ReEntry Compass is grounded in lived experience and driven by the belief that better reentry tools can change lives.





# ReEntry-Compass-Backend-Day-2-Setup
Document storage and the Reentry Resource directory. These represent the two core capabilities of the MVP.

Objectives:

    • Create MVP data models
    • Add Document upload capability
    • Add Resource directory records
    • Integrate models into admin panel
    • Establish basic homepage route



What Was Built:

1. Document Model

    • Represents files returning citizens need during reentry:
    • IDs
    • Housing documents
    • Employment paperwork
    • Legal documents
    • Health / MH records


Model fields include:

    • title
    • category
    • file upload
    • optional user association
    • timestamps
      
Purpose:

Build a secure centralized document vault one of the biggest unmet needs in reentry tech.

2. Resource Model

Stores support services available in housing, employment, legal, mental health, etc.

Fields include:

    • Name
    • Category
    • Address & City
    • State
    • Website
    • Felony-friendly indicator
    • Description & details
      
Purpose:
Create a trustworthy directory of verified reentry services.


3. Django Admin Integration
   
Both models were registered with filters, search, and list displays added to make the admin panel usable for early demos.
Admin now supports:
    • Uploading test documents
    • Entering resource providers
    • Searching & filtering resources

4. Static Media Configuration
   
Configured Django to store uploaded files under:
/media/documents/
Admin now supports live file uploads and organization.

5. Basic Homepage Added

A simple view was added to return a confirmation message at / so the backend no longer shows a 404.



Technical Skills Gained

    • Understanding Django models & ORM
    • Setting up media storage paths
    • Admin customization
    • URL routing
    • Local vs external IP handling
    • Live testing on a VPS


Summary
Day 2 created the first real features of ReEntry Compass:
    • A document vault
    • A resource directory
    • Admin tools for early MVP management
This brought the project to a working state where real reentry data structures exist and can be managed through Django’s admin dashboard.




Day 4 – User Authentication & Token Access

Summary
Built and verified the user authentication flow for the SaaS backend. Successfully logged in through the API, confirmed token-based authentication, and resolved access issues related to server connection context.

What Was Accomplished

Implemented user login functionality

Verified API authentication endpoint

Retrieved and validated authentication token

Confirmed secure access to protected backend features

Why This Matters
Authentication is a core SaaS feature. Token-based access allows users to stay securely logged in while protecting sensitive data and enabling future features like user roles, dashboards, and subscriptions.

Key Concepts

API-based authentication

Token-based login systems

Backend access control

SaaS security fundamentals
