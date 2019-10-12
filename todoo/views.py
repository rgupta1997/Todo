from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from todoo.models import Todoo
from todoo.serializers import TodooSerializer

@csrf_exempt
def todoo_list(request):
    if request.method=='GET':
        todoo= Todoo.objects.all()
        serializer=TodooSerializer(todoo,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=TodooSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,starus=400)

@csrf_exempt
def todoo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        todoo = Todoo.objects.get(pk=pk)
    except Todoo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodooSerializer(todoo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodooSerializer(todoo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todoo.delete()
        return HttpResponse(status=204)
# Create your views here.
