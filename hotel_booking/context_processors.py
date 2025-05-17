from django.conf import settings
import re


def site_info(request):
    WHATSAPP_PHONE = re.sub(r'\D', '', settings.SITE_PHONE)
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_EMAIL": settings.SITE_EMAIL,
        "SITE_PHONE": settings.SITE_PHONE,
        "SITE_ADDRESS": settings.SITE_ADDRESS,
        "CURRENCY_SYMBOL": settings.CURRENCY_SYMBOL,
        "CURRENCY_CODE": settings.CURRENCY_CODE,
        "WHATSAPP_PHONE": WHATSAPP_PHONE,
        "FACEBOOK_PAGE_LINK": settings.FACEBOOK_PAGE_LINK,
        "INSTAGRAM_PAGE_LINK": settings.INSTAGRAM_PAGE_LINK,
    }
