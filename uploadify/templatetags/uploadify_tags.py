from django import template
from uploadify import settings

register = template.Library()

# -----------------------------------------------------------------------------
#   multi_file_upload
# -----------------------------------------------------------------------------
@register.inclusion_tag('uploadify/multi_file_upload.html', takes_context=True)
def multi_file_upload(context, unique_id=None):
    """
    Displays a Flash-based interface for uploading multiple files.
    For each POST request (after file upload) send GET query with `unique_id`.
    """
    if unique_id is not None:
        GET_query = '?unique_id=' + str(unique_id)
    else:
        GET_query = ''
    return {
        'GET_query' : GET_query,
        'uploadify_path' : settings.UPLOADIFY_PATH,
    }
