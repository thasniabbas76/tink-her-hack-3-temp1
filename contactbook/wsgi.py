import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactbook.settings')

application = get_wsgi_application()

# Set the port dynamically based on Render's environment variable
port = os.getenv('PORT', '8000')  # Default to 8000 if PORT isn't set

# For debugging, you can print the port number to the console
print(f"Listening on port {port}")
