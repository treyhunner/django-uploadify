# -*- coding: utf-8 -*-

from uploadify import settings
from django.contrib.admin.widgets import AdminFileWidget
from django.template import RequestContext
from django.utils import simplejson
from django.template import loader
from django.utils.safestring import mark_safe

class UploadifyAdminWidget(AdminFileWidget):
    js = """
         <script type="text/javascript">
         $('#uploadify').bind('allUploadsComplete', function(data){
             window.location.reload();
         });
         </script>"""
    def __init__(self, *args, **kwargs):
        self.data = {}
        self.filename = 'Filename'
        if kwargs.has_key('attrs'):
            if kwargs['attrs'].has_key('data'):
                self.data = kwargs['attrs']['data']
                del kwargs['attrs']['data']
            if kwargs['attrs'].has_key('filename'):
                self.filename = kwargs['attrs']['filename']
                del kwargs['attrs']['filename']
        super(UploadifyAdminWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):

        self.data['fileDataName'] = self.filename

        output = {
            'uploadify_data' : simplejson.dumps(self.data),
            'uploadify_path' : settings.UPLOADIFY_PATH,
            'uploadify_filename' : self.filename,
        }

        template = 'uploadify/multi_file_upload.html'

        template_data = loader.render_to_string(template, output)

        template_data += self.js

        return mark_safe(template_data)
