from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments,Employees
from .serializers import DptSerializer,EmplySerializer


# Create your views here.
@csrf_exempt
def departmentApi(req, id=0):
	if req.method=='GET':
			departments = Departments.objects.all()
			departments_serializer = DptSerializer(departments,many=True)
			return JsonResponse(departments_serializer.data,safe=False)
	elif req.method == 'POST':
		department_data = JSONParser().parse(req)
		departments_serializer = DptSerializer(data=department_data)
		if departments_serializer.is_valid():
			departments_serializer.save()
			return JsonResponse('Added record Successfully',safe=False)
		return JsonResponse('Failed to add a record',safe=False)

