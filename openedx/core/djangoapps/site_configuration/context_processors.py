"""
Django template context processors.
"""
import urlparse

from django.conf import settings
from django.utils.http import urlquote_plus

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


def configuration_context(request):  # pylint: disable=unused-argument
    """
    Configuration context for django templates.
    """
    return {
        'platform_name': configuration_helpers.get_value('platform_name', settings.PLATFORM_NAME),
        'current_url': urlquote_plus(_absolute_current_url(request, request.path)),
        'current_site_url': urlquote_plus(_absolute_current_url(request, '/')),
    }


def _absolute_current_url(request, path):
    site_name = configuration_helpers.get_value('SITE_NAME', settings.SITE_NAME)
    parts = ("https" if request.is_secure() else "http", site_name, path, '', '', '')
    return urlparse.urlunparse(parts)
