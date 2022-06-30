from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register_new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Now you can log in")
    elif request.method == "GET":
        form = UserCreationForm()
    return render(request, 'useradmin/register_new_user.html', context={'form':form})