import os

# DJANGO SETTINGS
os.environ["SECRET_KEY"] = "your-secret-key-here"

# POSTGRESQL DATABASE URL
# os.environ.setdefault(
#     "DATABASE_URL", "postgresql://username:password@host:port/database_name"
# )

# for local postgresql database
os.environ["DATABASE_NAME"] = "hotel_booking"
os.environ["DATABASE_USER"] = "postgres"
os.environ["DATABASE_PASSWORD"] = "root"
os.environ["DATABASE_HOST"] = "localhost"
os.environ["DATABASE_PORT"] = "5432"

# STRIPE SETTINGS
os.environ["STRIPE_SECRET_KEY"] = "your-stripe-secret-key"
os.environ["STRIPE_PUBLIC_KEY"] = "your-stripe-public-key"

# CLOUDINARY URL
os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://api_key:api_secret@cloud_name"
)

# SITE DETAILS
os.environ["SITE_NAME"] = "Your Hotel Name"
os.environ["SITE_EMAIL"] = "info@yourhotel.com"
os.environ["SITE_PHONE"] = "+44 1234 567890"
os.environ["SITE_ADDRESS"] = "Your Hotel Address"

# Social Media Links
os.environ["FACEBOOK_PAGE_LINK"] = "https://www.facebook.com/your-hotel-page"
os.environ["INSTAGRAM_PAGE_LINK"] = "https://www.instagram.com/your-hotel-page"

# Currency Configuration
os.environ["CURRENCY_SYMBOL"] = "GBP"
os.environ["CURRENCY_CODE"] = "GBP"

# Email Configuration
os.environ['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
os.environ['EMAIL_HOST'] = 'your-smtp-server.com'
os.environ['EMAIL_PORT'] = '465'
os.environ['EMAIL_USE_TLS'] = 'False'
os.environ['EMAIL_USE_SSL'] = 'True'
os.environ['EMAIL_HOST_USER'] = 'your-email@example.com'
os.environ['EMAIL_HOST_PASSWORD'] = 'your-email-password'
os.environ['DEFAULT_FROM_EMAIL'] = 'your-email@example.com'
