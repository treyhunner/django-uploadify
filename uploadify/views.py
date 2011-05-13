from django.dispatch import Signal
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from sugar.views.json import JsonResponse
from misc.json_encode import json_response

upload_received = Signal(providing_args=['request', 'data'])

@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        sender = request.POST.get('sender', 'uploadify')
        filename = request.POST.get('fileDataName', 'Filename')
        if request.FILES:
            received_list = upload_received.send(sender=sender, request=request,
                data=request.FILES[filename])
            for received, response in received_list:
                if response is not None:
                    return json_response({filename: response})
    return HttpResponse('1')
