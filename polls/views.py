# views.py

from django.http import JsonResponse
from polls.tasks import process_data
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_data(request):
    # Example data to be processed
    data = request.POST.get('data', 'default data')
    # Send the task to the queue without waiting for it to complete
    process_data.delay(data)
    print("yo")
    # Respond immediately
    return JsonResponse({'status': 'Data is being processed', 'data': data})