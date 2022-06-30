from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from student.models import Student
from student.serializer import StudentSerializer

'''
Method 1 : (Using ViewSet class)
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("***********List************")
        print("BaseName :",self.basename)
        print("Action : ",self.action)
        print("Detail : ",self.detail)
        print("Suffix : ",self.suffix)
        print("Name ; ",self.name)
        print("Description : ",self.description)
        stu = Student.objects.all()
        serializer =StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk = None):
        print("***********Retrieve************")
        print("BaseName :", self.basename)
        print("Action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("Name ; ", self.name)
        print("Description : ", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response (serializer.data)

    def create(self,request):
        print("***********Create************")
        print("BaseName :", self.basename)
        print("Action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("Name ; ", self.name)
        print("Description : ", self.description)
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        print("***********Update************")
        print("BaseName :", self.basename)
        print("Action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("Name ; ", self.name)
        print("Description : ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update (self,request,pk):
        print("***********Partial Update************")
        print("BaseName :", self.basename)
        print("Action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("Name ; ", self.name)
        print("Description : ", self.description)
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        print("***********Destroy************")
        print("BaseName :", self.basename)
        print("Action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("Name ; ", self.name)
        print("Description : ", self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
'''

'''
# Method 2 (using ModelViewSet class)
#-----------
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''

#Method 3 (using ReadOnlyModelViewSet class)
#-----------
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

