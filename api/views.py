from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .excel_helpers import read_excel

# Create your views here.
@api_view(['GET'])
def status(request):
	return Response({'status': 'ok'})

@api_view(['GET', 'POST'])
def import_xls(request):
	if request.method == 'POST':
		file = request.FILES.get('file')
		if (file):
			data = read_excel(file)
			print(data)
		else:
			print('File not found')
	return redirect('test_app:index')
	# return Response({'status': 'ok'})