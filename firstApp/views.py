from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Student
from .serializers import StudentSerializer,StudentModelSerializer
# Create your views here.

class StudentListView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentModelSerializer

class StudentListCreateView(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentModelSerializer

    
    def get_queryset(self):
        return self.queryset.filter(email__icontains="yahoo")

class GraduatingStudents(generics.GenericAPIView):
    serializer_class=StudentModelSerializer
    queryset=Student.objects.all()
    def get(self, request, *args , **kwargs):
        query_set=self.get_queryset().filter(email__icontains="gmail")
        serializer=self.serializer_class(query_set, many=True)
        return Response({'message':'getting graduating students','data':serializer.data},status=status.HTTP_200_OK)

class StudentList(APIView):
    # def get (self, request, *args , **kwargs):
        # students = Student.objects.all()
        # # serializer = StudentSerializer(students, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)



    def post (self, request, *args, **kwargs):
        user_data = request.data 
        serializer =  StudentModelSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetails(APIView):
    def get (self, pk):
        try:
            student=Student.objects.get(id=pk)
            return student
        except Student.DoesNotExist:
            raise Http404
        
    def get (self, request, pk):
        student=self.get_object()
        serializer=StudentModelSerializer(student)
        return Response(serializer.data, status=status.HTTP_202_OK)

    def delete(self, request, pk):
        student=self.get_object()
        student.delete()
        return Response({'message':'student deleted successfully'}, status=status.HTTP_204_NO_CONTENT) 
