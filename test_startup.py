import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContactList.settings')
os.environ['DEBUG'] = 'True'

try:
    import django
    print("✓ Django imported")
    
    django.setup()
    print("✓ Django setup successful")
    
    from django.urls import reverse
    print("✓ URLs imported")
    
    from contacts.models import Contact
    print("✓ Models imported")
    
    print("\nAll startup checks passed!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
