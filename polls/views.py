# views.py

from django.http import JsonResponse
from polls.tasks import process_data
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from .forms import ResumeForm

@csrf_exempt
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your actual success URL
    else:
        form = ResumeForm()
    return render(request, 'polls/upload_resume.html', {'form': form})

@csrf_exempt
def send_data(request):
    # Example data to be processed
    data = request.POST.get('data', 'default data')
    # Send the task to the queue without waiting for it to complete
    process_data.delay(data)
    print("yo")
    # Respond immediately
    return JsonResponse({'status': 'Data is being processed', 'data': data})