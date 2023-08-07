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
