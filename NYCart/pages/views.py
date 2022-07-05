from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import NewVendorForm
from django.apps import apps

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def vendorList(request):
    vendormodel = apps.get_model('app_api', 'Vendor')
    vendors = vendormodel.objects.all()
    vendors_dict = {
        'vendors': vendors
    }
    return render(request, 'pages/vendor_grid.html', vendors_dict)

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
