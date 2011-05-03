from django import template
from uploadify import settings
from django.utils import simplejson

register = template.Library()

# -----------------------------------------------------------------------------
#   multi_file_upload
# -----------------------------------------------------------------------------
class MultiFileUpload(template.Node):
    def __init__(self, sender='uploadify', unique_id=None, options={}, data={}):
        self.sender = sender
        self.unique_id = unique_id
        self.options = {'fileDataName': 'Filedata'}
        self.options.update(options)
        self.data = {'fileDataName': self.options['fileDataName'],
                     'sender': str(self.sender)}
        self.data.update(data)

    def render(self, context):
        if self.unique_id is not None:
            unique_id = "?unique_id=%s" % str(self.unique_id)
        else:
            unique_id = ""

        js_options = ",".join(map(lambda k: "'%s': '%s'" % (k, self.options[k]),
                                  self.options))

        auto = False
        if self.options.has_key('auto') and self.options['auto']:
            auto = True

        context.update({
            'uploadify_query': unique_id,
            'uploadify_data': simplejson.dumps(self.data),
            'uploadify_path': settings.UPLOADIFY_PATH,
            'uploadify_options': js_options,
            'uploadify_filename': self.options['fileDataName'],
            'uploadify_auto': auto,
        })

        t = template.loader.get_template('uploadify/multi_file_upload.html')
        return t.render(context)


@register.tag
def multi_file_upload(parser, token):
    """
    Displays a Flash-based interface for uploading multiple files.
    For each POST request (after file upload) send GET query with `unique_id`.

    {% multi_file_upload sender='SomeThing' fileDataName='Filename' %}

    For all options see http://www.uploadify.com/documentation/

    """
    args = token.split_contents()
    tag_name = args[0]
    args = args[1:]

    sender = 'uploadify'
    unique_id = None
    options = {}

    for arg in args:
        name, val = arg.split("=")
        val = val.replace('\'', '').replace('"', '')
        if name == 'sender':
            sender = val
        elif name == 'unique_id':
            unique_id = val
        else:
            options[name] = val

    return MultiFileUpload(sender, unique_id, options)

