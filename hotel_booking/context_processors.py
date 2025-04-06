from django.conf import settings

def site_info(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_EMAIL": settings.SITE_EMAIL,
        "SITE_PHONE": settings.SITE_PHONE,
        "SITE_ADDRESS": settings.SITE_ADDRESS,
    }
