#!/usr/bin/env python
"""
Create a Django superuser/admin account
Run this script to create an admin account for your Railway PostgreSQL database
"""
import os
import sys
import django

# Add the project to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContactList.settings')
django.setup()

from django.contrib.auth.models import User
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def create_admin():
    """Create a superuser account"""
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')
    
    print(f"Creating superuser with username: {username}")
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"✗ Superuser '{username}' already exists")
        return False
    
    try:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✓ Superuser '{username}' created successfully!")
        print(f"  Email: {email}")
        print(f"  Password: {password}")
        print("\nYou can now login at: /admin/")
        return True
    except Exception as e:
        print(f"✗ Error creating superuser: {e}")
        return False

if __name__ == '__main__':
    success = create_admin()
    sys.exit(0 if success else 1)
