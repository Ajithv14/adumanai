from django.http import HttpResponse
from .models import cakes_collections

import datetime



def index(request):
    cakes = cakes_collections.find()
    return HttpResponse(cakes)

def push_data(request):
    cake = {
        "name": "Black forest",
        "description": "Black forest description",
        "tags": ["mongodb", "python", "pymongo"],
        "price": "350",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Black_Forest_gateau.jpg/1280px-Black_Forest_gateau.jpg",
        "datetime": datetime.datetime.utcnow()
    }

    cake_id = cakes_collections.insert_one(cake).inserted_id
    out=(f'posted data successfully {cake_id}')
    return HttpResponse(out)