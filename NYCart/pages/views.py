from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import NewVendorForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

class addVendor(View):
    form_class = NewVendorForm
    template_name ='pages/new_vendor_form.html'

    def get(self, request, *args, **kwargs):
        form = NewVendorForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})