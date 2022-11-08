from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index_page(request):
    return render(request, 'index.html')

@require_http_methods(['GET'])
def chat_list(request):
    return JsonResponse({ "chats": [] })

@require_http_methods(['GET'])
def chat_page(request, id):
    return JsonResponse({ "chat_id": id})

@require_http_methods(['POST'])
def chat_create(request):
    return JsonResponse({'create': True})
