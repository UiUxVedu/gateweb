from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from django.contrib.auth.decorators import user_passes_test


# HOME PAGE
def home(request):
    return render(request, 'home/home.html')

# ADD APPLICATION
def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()

            # Redirect based on course
            course = application.course

            if course == 'CS':
                return redirect('info_cs')
            elif course == 'ENTC':
                return redirect('info_entc')
            elif course == 'EE':
                return redirect('info_elec')
            elif course == 'ME':
                return redirect('info_mech')

            return redirect('home')

    else:
        form = ApplicationForm()

    return render(request, 'applications/add.html', {'form': form})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def application_list(request):
    applications = Application.objects.all().order_by('-created_at')
    return render(request, 'applications/list.html', {
        'applications': applications
    })

# INFO PAGES
def info_cs(request):
    return render(request, 'info/info_cs.html')

def info_entc(request):
    return render(request, 'info/info_entc.html')

def info_elec(request):
    return render(request, 'info/info_elec.html')

def info_mech(request):
    return render(request, 'info/info_mech.html')
