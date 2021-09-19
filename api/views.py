from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def status(request):
	return Response({'status': 'ok'})