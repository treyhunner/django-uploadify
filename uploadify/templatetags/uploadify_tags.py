from django import template
from uploadify import settings
from django.utils import simplejson

register = template.Library()

# -----------------------------------------------------------------------------
#   multi_file_upload
# -----------------------------------------------------------------------------
@register.inclusion_tag('uploadify/multi_file_upload.html', takes_context=True)
def multi_file_upload(context, sender=None, filename='Filename', unique_id=None):
    """
    Displays a Flash-based interface for uploading multiple files.
    For each POST request (after file upload) send GET query with `unique_id`.
    """
    data = {'fileDataName': filename}

    if sender is not None:
        data['sender'] = str(sender)

    if unique_id is not None:
        unique_id = "?unique_id=%s" % str(unique_id)
    else:
        unique_id = ""

    return {
        'uploadify_query' : unique_id,
        'uploadify_data' : simplejson.dumps(data),
        'uploadify_path' : settings.UPLOADIFY_PATH,
        'uploadify_filename' : filename,
    }
