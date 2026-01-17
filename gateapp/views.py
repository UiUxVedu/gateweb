from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudentApplication
from .forms import StudentApplicationForm

def index(request):
    applications = StudentApplication.objects.all().order_by('-applied_at')
    return render(request, 'index.html', {'applications': applications})

def add(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted successfully")
            return redirect('/')
    else:
        form = StudentApplicationForm()
    return render(request, 'add.html', {'form': form})

@login_required
def update(request, id):
    application = get_object_or_404(StudentApplication, id=id)
    if request.method == 'POST':
        application.status = request.POST.get('status')
        application.save()
        messages.success(request, "Status updated successfully")
        return redirect('/')
    return render(request, 'update.html', {'application': application})

@login_required
def delete(request, id):
    application = get_object_or_404(StudentApplication, id=id)
    application.delete()
    messages.success(request, "Application deleted")
    return redirect('/')

def filter_details(request):
    applications = StudentApplication.objects.all()
    course = request.GET.get('course')
    status = request.GET.get('status')
    country = request.GET.get('country')

    if course:
        applications = applications.filter(course=course)
    if status:
        applications = applications.filter(status=status)
    if country:
        applications = applications.filter(country__icontains=country)

    return render(request, 'filter_details.html', {'applications': applications})
