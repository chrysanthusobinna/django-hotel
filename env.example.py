import os

# DJANGO SETTINGS
os.environ["SECRET_KEY"] = "your-django-secret-key"
os.environ["DEBUG"] = "False"

# STRIPE SETTINGS
os.environ["STRIPE_SECRET_KEY"] = "your-stripe-secret-key"
os.environ["STRIPE_PUBLIC_KEY"] = "your-stripe-public-key"

# CLOUDINARY URL
os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://your-cloudinary-key@your-cloud-name"
)

os.environ["USE_CLOUDINARY"] = "True"

# SITE DETAILS
os.environ["SITE_NAME"] = "Santhus Hotel"
os.environ["SITE_EMAIL"] = "info@yourdomain.com"
os.environ["SITE_PHONE"] = "+44 0000 000000"
os.environ["SITE_ADDRESS"] = "Your Address"

# EMAIL SETTINGS (Example: Gmail or any SMTP)
os.environ['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
os.environ['EMAIL_HOST'] = 'your.smtp.server.com'
os.environ['EMAIL_PORT'] = '587'
os.environ['EMAIL_USE_TLS'] = 'True'
os.environ['EMAIL_HOST_USER'] = 'your-email@domain.com'
os.environ['EMAIL_HOST_PASSWORD'] = 'your-email-password'
os.environ['DEFAULT_FROM_EMAIL'] = 'your-email@domain.com'
