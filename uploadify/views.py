from django.dispatch import Signal
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

upload_received = Signal(providing_args=['request', 'data'])

@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            file_url = upload_received.send(sender='uploadify', request=request,
                data=request.FILES['Filedata'])[-1][1]
            return HttpResponse(file_url)
    return HttpResponse('1')
