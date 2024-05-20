from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    return JsonResponse({"message":"This is a message from first every api created by Pawan."})