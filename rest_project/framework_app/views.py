from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from rest_framework import status

# Create your views here.
class startingPage(View):
    def get(self,request):
        employees = Employee.objects.all()
        form = EmployeeForm()
        return render(request,'framework_app/index.html',{"employess":employees,"form":form})
    
    def post(self,request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('form'))
        return render(request,'framework_app/index.html',{"error":"You have not filled form correctly.","form":form})

class employee(APIView):
    def get(self,request,id):
        if id:
            employee = Employee.objects.get(pk=id)
            serializer = EmployeeSerializer(employee)
            return Response({'status':"200","data":serializer.data})
        employees = Employee.objects.all()
        print(employees)
        serializer = EmployeeSerializer(employees,many=True)
        return Response({'status':"200","data":serializer.data})
   
    def post(self,request):
        new_data = EmployeeSerializer(data = request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({'status':'success',"data":new_data.data},status=status.HTTP_200_OK)    
        return Response({'status':'error','data':new_data.errors})
    
    def patch(self,request,id):
        employee = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        return Response({'status':'error','error':serializer.errors})
    
    def delete(self,request,id):
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return Response({'status':'success','message':'Record deleted'})
  