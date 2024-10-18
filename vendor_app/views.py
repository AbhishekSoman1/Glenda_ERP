from django.shortcuts import render, redirect

from Glenda_App.models import Menu
from register_app.forms import CustomUserForm
from django.contrib import messages

from register_app.models import CustomUser
from vendor_app.forms import VendorRegisterForm


# Create your views here.

def view_vendor_list(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    view=CustomUser.objects.filter(is_staff=False)

    return render(request,'vendor/view_vendor_list.html',{'view':view,'menus':menus})



def vender_register_view(request):
    # Fetching menus and their related submenus for display
    menus = Menu.objects.prefetch_related('submenus').all()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('view_vendor_list')
        messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserForm()
    return render(request, 'vendor/vendor_reg.html', {'form': form, 'menus': menus})

def create_vendor_details(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = VendorRegisterForm(request.POST, request.FILES)  # Added request.FILES for file uploads if needed
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user_id = id  # Associate the user
            vendor.save()
            form.save_m2m()  # Save the many-to-many field for materials
            return redirect('vender_list')  # Redirect to vendor list after successful submission
    else:
        form = VendorRegisterForm()

    return render(request, 'vendor/add_vendor_details.html', {'form': form, 'menus': menus})
