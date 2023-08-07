from rest_framework import serializers as s
from .models import Departments, Employees


class DptSerializer(s.ModelSerializer):
	class Meta:
		model = Departments
		field = ('DepartmentId', 'DepartmentName')


class EmplySerializer(s.ModelSerializer):
	class Meta:
		models = Employees
		fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
