from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
	path('status', views.status, name='status'),
	path('import_xls', views.import_xls, name='import_xls'),
]