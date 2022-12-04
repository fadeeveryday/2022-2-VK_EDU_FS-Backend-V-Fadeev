import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from chats.models import Chats
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


def parse_request(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return {
            'ok': False,
            'result': 'wrong json format'
        }
    return {
        'ok': True,
        'data': data
    }


# curl -X PUT -d '{"chat_id": 1, "title": "title", "description": "test chat", "author_id": 1}' 'http://127.0.0.1:8000/chats/update_chat/'
@require_http_methods(['PUT'])
def update_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        chat = Chats.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })
    title = data.get('title')
    description = data.get('description')
    author_id = data.get('author_id')

    if title is not None:
        chat.title = title

    if description is not None:
        chat.description = description

    if author_id is not None:
        try:
            author = User.objects.get(id=author_id)
        except (ObjectDoesNotExist, ValueError):
            return JsonResponse({
                'ok': False,
                'code': 404,
                'result': f'user with id={author_id} does not exists'
            })
        chat.author = author

    chat.save()

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


# curl -X GET -d '{"user_id": 1}' 'http://127.0.0.1:8000/chats/get_all_chats/'
@require_http_methods(['GET'])
def get_all_chats(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    user_id = data['user_id']
    try:
        author = User.objects.get(id=user_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={user_id} does not exists'
        })
    try:
        chats = Chats.objects.filter(author=author)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'no chats where author is {author.username}'
        })
    response = {}
    for chat in chats:
        response[chat.id] = {
            'title': chat.title,
            'description': chat.description,
            'author_id': chat.author.id
        }

    return JsonResponse({
        'ok': True,
        'code': 200,
        'result': response
    })


# curl -X GET -d '{"chat_id": 1}' 'http://127.0.0.1:8000/chats/get_chat/'
@require_http_methods(['GET'])
def get_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        chat = Chats.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    members = User.objects.filter(chats__id=chat_id).values()

    return JsonResponse({
        'ok': True,
        'code': 200,
        'result': {
            'id': chat.id,
            'title': chat.title,
            'description': chat.description,
            'author_id': chat.author.id,
            'members': list(members),
        }
    })


# curl -d '{"title": "title", "description": "test chat", "author_id": 1}' 'http://127.0.0.1:8000/chats/create_chat/'
@require_http_methods(['POST'])
def create_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    title = data.get('title')
    description = data.get('description')
    author_id = data.get('author_id')
    try:
        author = User.objects.get(id=author_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={author_id} does not exists'
        })

    Chats.objects.create(title=title, description=description, author=author)

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


# curl -d '{"chat_id": 2}' 'http://127.0.0.1:8000/chats/delete_chat/'
@require_http_methods(['POST'])
def delete_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        Chats.objects.get(id=chat_id).delete()
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


@require_http_methods(['GET'])
def start_page(request):
    return render(request, 'index.html')