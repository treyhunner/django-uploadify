from django.dispatch import Signal
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sugar.views.json import JsonResponse

upload_received = Signal(providing_args=['request', 'data'])

@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        sender='uploadify'
        if request.POST.has_key('sender'):
            sender = request.POST['sender']
        if request.FILES:
            receiveds = upload_received.send(sender=sender, request=request,
                data=request.FILES['file'])
            for received, response in receiveds:
                if not response is None:
                    return JsonResponse(response)
    return HttpResponse('1')
