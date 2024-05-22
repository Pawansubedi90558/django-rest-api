from django.http import JsonResponse
import json

#without DRF
# from products.models import Product
# from django.forms.models import model_to_dict
"""def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        """serialization is done below i.e. a model instance(model_data) is converted into python dictionary and then returned as JSON to the client
        data['id'] =  model_data.id
        data['check'] = True
        data['title'] =  model_data.title
        data['content'] = model_data.content
        data['price'] =  model_data.price
    the above can also be done using model_to_dict method where we can specify the specific fields to be taken
        data = model_to_dict(model_data, fields=['id','title'])
    return JsonResponse(data)""""""
#using rest framework
from rest_framework.response import Response
from rest_framwork.decorators import api_view

@api_view
def api_home():
    model_data = Product.objects.all().order_by("?").first()
    


        

"""
{'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'localhost:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
"""