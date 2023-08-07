from django.db import models as m


# Create your models here.
class Departments(m.Model):
	DepartmentId = m.AutoField(primary_key=True)
	DepartmentName = m.CharField(max_length=300)


class Employees(m.Model):
	EmployeeId = m.AutoField(primary_key=True)
	EmployeeName = m.CharField(max_length=500)
	Department = m.CharField(max_length=500)
	DateOfJoining = m.DateTimeField()
	PhotoFileName = m.CharField(max_length=500)

