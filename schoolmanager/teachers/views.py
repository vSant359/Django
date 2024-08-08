from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Teachers
import json


class TeacherListView(View):
    def get(self, request):
        teachers = list(Teachers.objects.values())
        return JsonResponse(teachers, safe=False)
    
    
    @method_decorator(csrf_exempt, name="dispatch")
    def post(self, request):
        data = json.loads(request.body)
        teacher = Teachers.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            speciality=data['speciality']
        )
        return JsonResponse({"id": teacher.id, "name": teacher.first_name, "message": "Teacher created successfully"})

class TeacherDetailView(View):
    def get(self, request, pk):
        try:
            teacher = Teachers.objects.get(pk=pk)
            return JsonResponse({
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "email": teacher.email,
                "speciality": teacher.speciality,
            })
        except Teachers.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)
    
    @csrf_exempt
    def put(self, request, pk):
        try:
            teacher = Teachers.objects.get(pk=pk)
            data = json.loads(request.body)
            
            if 'first_name' in data:
                teacher.first_name = data['first_name']
            if 'last_name' in data:
                teacher.last_name = data['last_name']
            if 'email' in data:
                teacher.email = data['email']
            if 'speciality' in data:
                teacher.speciality = data['speciality']
            
            teacher.save()
            return JsonResponse({"message": "Teacher updated successfully"})
        except Teachers.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)

    @csrf_exempt
    def delete(self, request, pk):
        try:
            teacher = Teachers.objects.get(pk=pk)
            teacher.delete()
            return JsonResponse({"message": "Teacher deleted successfully"})
        except Teachers.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)
