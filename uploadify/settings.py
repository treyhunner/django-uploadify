from django.conf import settings
STATIC_UR:L = getattr(settings, 'STATIC_URL', '')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '')

# Uploadify root folder path, relative to MEDIA_
UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_PATH', 
    '%s%s' % (STATIC_URL, 'js/uploadify/'))

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', 
    '%s%s' % (MEDIA_URL, 'uploads/'))
