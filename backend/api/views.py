from django.http import JsonResponse
import json
from products.models import Product

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #serialization is done below i.e. a model instance(model_data) is converted into python dictionary and then returned as JSON to the client
        data['id'] =  model_data.id
        data['check'] = True
        data['title'] =  model_data.title
        data['content'] = model_data.content
        data['price'] =  model_data.price
    return JsonResponse(data)

"""
{'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'localhost:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
"""