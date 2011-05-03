# -*- coding: utf-8 -*-

from uploadify import settings
from django.contrib.admin.widgets import AdminFileWidget
from uploadify.templatetags.uploadify_tags import MultiFileUpload
from django.utils.safestring import mark_safe
from django.template import Context

class UploadifyAdminWidget(AdminFileWidget):
    """
    Create uploadify widget. It receive:
        'sender' - string (default = uploadify)
        'unique_id'
        'options' - http://www.uploadify.com/documentation/
        'data' - POST data

    Example:
        self.fields['uploadify'].widget = UploadifyAdminWidget(
                    attrs={'data': post_data, 'options': {'fileDataName': 'image'}})
    """

    js = """
         <script type="text/javascript">
         $('#uploadify').bind('allUploadsComplete', function(data){
             window.location.reload();
         });
         </script>"""

    def __init__(self, *args, **kwargs):
        self.sender = 'uploadify'
        self.unique_id = None
        self.options = {}
        self.data = {}

        if kwargs.has_key('attrs'):
            for attr in kwargs['attrs']:
                if attr in ('sender', 'unique_id', 'options', 'data'):
                    setattr(self, attr, kwargs['attrs'][attr])
        super(UploadifyAdminWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        context = Context({})
        uploader = MultiFileUpload(self.sender, self.unique_id, self.options, self.data)
        template_data = uploader.render(context)
        template_data += self.js

        return mark_safe(template_data)
