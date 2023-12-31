from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee,Song,Singer
from .serializer import EmployeeSerializer,SongSerializer,SingerSerializer
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework import viewsets

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

# class employee(APIView):
#     def get(self,request,id):
#         if id:
#             employee = Employee.objects.get(pk=id)
#             serializer = EmployeeSerializer(employee)
#             return Response({'status':"200","data":serializer.data})
#         employees = Employee.objects.all()
#         print(employees)
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response({'status':"200","data":serializer.data})
   
#     def post(self,request): 
#         new_data = EmployeeSerializer(data = request.data)
#         if new_data.is_valid():
#             new_data.save()
#             return Response({'status':'success',"data":new_data.data},status=status.HTTP_200_OK)    
#         return Response({'status':'error','data':new_data.errors})
    
#     def patch(self,request,id):
#         employee = Employee.objects.get(pk=id)
#         serializer = EmployeeSerializer(employee,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'success','data':serializer.data})
#         return Response({'status':'error','error':serializer.errors})
    
#     def delete(self,request,id):
#         employee = Employee.objects.get(pk=id)
#         employee.delete()
#         return Response({'status':'success','message':'Record deleted'})
  

class Employee(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)  
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)  
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)  
    

# class Employee(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()    
#     serializer_class = EmployeeSerializer

class SingerView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongView(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer    
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)