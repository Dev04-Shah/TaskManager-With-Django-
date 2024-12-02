from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tasks

def home(request):
    if request.method == "POST":
        try:
            task_name = request.POST.get('task_name')
            client_image = request.FILES.get('client_image')
            task_image = request.FILES.get('task_image')
            video = request.POST.get('video')
            remarks = request.POST.get('remarks')
            
            # Create and save the task
            task = Tasks.objects.create(
                task_name=task_name,
                client_image=client_image,
                task_image=task_image,
                video=video,
                remarks=remarks
            )
            
            return redirect('home')  # Redirect to home after successful submission
            
        except Exception as e:
            print(f"Error: {e}")
            # You might want to add an error message here
    
    # Handle GET request and search
    search_term = request.GET.get('searchTask', '')
    if search_term:
        tasks = Tasks.objects.filter(task_name__icontains=search_term)
    else:
        tasks = Tasks.objects.all()
    
    return render(request, 'home.html', {'task': tasks, 'searchTerm': search_term})

