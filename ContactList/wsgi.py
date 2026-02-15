"""
WSGI config for ContactList project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application

# Configure logging to see startup errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContactList.settings')

try:
    logger.info("=" * 60)
    logger.info("ContactManager WSGI Application Starting")
    logger.info("=" * 60)
    logger.info(f"DEBUG: {os.getenv('DEBUG', 'Not set')}")
    logger.info(f"DATABASE_URL: {'Set' if os.getenv('DATABASE_URL') else 'Not set'}")
    logger.info(f"SECRET_KEY: {'Set' if os.getenv('SECRET_KEY') else 'Using default'}")
    logger.info("Loading Django WSGI application...")
    
    application = get_wsgi_application()
    
    logger.info("✓ Django WSGI application loaded successfully")
    logger.info("=" * 60)
    
except Exception as e:
    logger.critical(f"✗ Failed to load Django WSGI application", exc_info=True)
    raise
