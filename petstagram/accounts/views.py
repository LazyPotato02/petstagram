from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, template_name='register-page.html')


def login(request):
    return render(request, template_name='login-page.html')


def show_profile_details(request, pk):
    return render(request, template_name='profile-details-page.html')


def profile_edit(request, pk):
    return render(request, template_name='profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, template_name='profile-delete-page.html')
