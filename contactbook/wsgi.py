import os
from django.core.wsgi import get_wsgi_application

# Use the environment variable PORT if set, or default to 8000
port = os.getenv("PORT", "8000")

# Bind to the port (Render dynamically sets this)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contactbook.settings")

application = get_wsgi_application()