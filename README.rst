This branch aims to add support for the soon to be released Django 1.3.

django-uploadify
================

A "Django":http://www.djangoproject.com/ re-usable app to integrate "Uploadify":http://www.uploadify.com/.

Installation
============

Installing django-uploadify
---------------------------

# "Download django-uploadify":http://github.com/tstone/django-uploadify/downloads
# Place the folder 'uploadify' somewhere on your Python path (either in your project directory or inside of Python26\Lib\site-packages\).
# Add 'uploadify' to your INSTALLED_APPS in your project's settings.py file
# Add a reference to uploadify in your urls.py...
<code>(r'^uploadify/', include('uploadify.urls')),</code>

Installing Uploadify
--------------------

# "Download uploadify":http://www.google.com/url?q=http://www.uploadify.com/
# Copy all of the 'uploadify' folder from the Uploadify distribution into your media root.  Default is: MEDIA_URL\js\uploadify\
# Rename the uploadify file from "jquery.uploadify.v2.1.0.min.js" (or whatever version it is) to simply "jquery.uploadify.js"
# In uploadify/settings.py, make sure the setting UPLOADIFY_PATH is set to the correct value if the uploadify folder is installed to a location other than the default.  Note that the UPLOADIFY_PATH setting is relative to the MEDIA_URL value.

Requrements
-----------

* django
* django-misc

Using django-uploadify
======================

How It Works
------------

Django-uploadify works by providing a template tag, {% multi_file_upload <upload_complete_url> %}., which takes a single parameter.  The template tag will render the Uploadify jquery/flash multi-file upload interface on the page.  A user may operate Uploadify, selecting and uploading multiple files.  For each file that is uploaded a Django signal will be fired, containing the file data.  After all uploads have been completed, the template tag will use the value of 'upload_complete_url'.  It will fetch that page via AJAX, and replace the Uploadify GUI with the contents of the page (a jQuery $.load).

Code Examples
-------------

To insert the django-uploadify template tag... ::
    
    {% load uploadify_tags %}{% multi_file_upload '/your/url/upload/complete/' %}

Creating a signal receiver... ::

    def upload_received_handler(sender, data, **kwargs):
        if file:
            # process the received file here
            print data.file

    upload_recieved.connect(upload_received_handler, dispatch_uid='yourapp.whatever.upload_received')</pre>

Making it all work
------------------

More than likely the ideal use is to tie the upload_received signal to automatically create a new object with Django's ORM.  If you're planning on having an edit interface of any sort for the users after upload is complete (ideally what would be in 'upload_complete_url'), an additional object property to keep track of this would work well.

Say we want to make a photo sharing app where users can upload several photos.  In our media manager app, we could have a model like so... ::

    class Media(models.Model):
        file = models.FileField(upload_to='upload')
        new_upload = models.BooleanField()</pre>

Whenever a signal is received, we can have the signal handler create a new instance of the object... ::

    def upload_received_handler(sender, data, **kwargs):
        if file:
            new_media = Media.objects.create(
                file = data,
                new_upload = True,
            )
            new_media.save()

    upload_recieved.connect(upload_received_handler, dispatch_uid='happenings.models.upload_received')</pre>

Finally, the value of 'upload_complete_url' sends the users to a view which finds all of the files with new_upload = True.  (I'll leave it up to you to figure out how you want to associate media objects with users).

Reference
=========

Client Side Event:  allUploadsComplete
On the client side, a javascript event is provided to capture when all uploads have been completed.  It can be bound with the following jQuery code:
<pre>$('#uploadify').bind('allUploadsComplete', function(e, data){
     // This code executes on AllUploadsComplete event...
}</pre>

<h3>upload_complete_url Parameter</h3>
When this page is fetched by the client-side javascript, the following Uploadify values are POST'ed to it:
    * filesUploaded - The total number of files uploaded
    * errors - The total number of errors while uploading
    * allBytesLoaded - The total number of bytes uploaded
    * speed - The average speed of all uploaded files
