from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def message_id(request):
    try:
        message_id = request.GET.get('massage_id')
        message = message_id.objects.get(message_id)
    except message_id.DoesNotExist:
        raise Http404
    return JsonResponse(message.description)