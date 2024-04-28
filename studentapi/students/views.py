from venv import logger
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .services import StudentService  # We'll define this service layer to handle logic

@require_http_methods(["GET"])
def get_all_students(request):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    students, total = StudentService.get_all_students(page, limit)
    return JsonResponse({
        'students': students,
        'total': total
    }, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def add_students_from_csv(request):
    try:
        csv_file = request.FILES.get('studentcsv')
        if not csv_file:
            return JsonResponse({'error': 'No file provided'}, status=400)
        
        # Decode the file before processing
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        
        # Process the CSV file
        created_students, message = StudentService.add_students_from_csv(decoded_file)
        
        if created_students is None:
            return JsonResponse({'error': message}, status=400)
        
        students_data = [model_to_dict(student) for student in created_students]
        return JsonResponse({'message': 'Students added successfully','Info': message,'details': students_data}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["DELETE"])
def delete_all_students(request):
    count = StudentService.delete_all_students()
    return JsonResponse({'message': f'Deleted {count[0]} students successfully'})
