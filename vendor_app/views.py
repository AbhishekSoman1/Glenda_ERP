import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Glenda_App.models import Menu
from register_app.forms import CustomUserForm
from django.contrib import messages

from register_app.models import CustomUser
from vendor_app.forms import VendorRegisterForm
from vendor_app.models import vendor_register


# Create your views here.

def view_vendor_list(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    view=CustomUser.objects.filter(is_staff=False)

    return render(request,'vendor/view_vendor_list.html',{'view':view,'menus':menus})

def view_vendor_profile(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()

    view = vendor_register.objects.filter(user_id=id)

    return render(request,'vendor/view_vendor_profile.html',{'view':view,'menus':menus})

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
            return redirect('view_vendor_list')  # Redirect to vendor list after successful submission
    else:
        form = VendorRegisterForm()

    return render(request, 'vendor/add_vendor_details.html', {'form': form, 'menus': menus})



def vendor_details_pdf(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()
    view = vendor_register.objects.filter(user_id=id).first()

    context = {'view': view, 'menu': menus}
    template = get_template('vendor/vendor_details_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="vendor_profile_{view.user.name}.pdf"'

    pdf_status = pisa.CreatePDF(
        html,
        dest=response
    )
    return response


def vendor_list_csv(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    view = CustomUser.objects.filter(is_staff=False)

    context = {'view': view, 'menu': menus}
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = f'attachment; filename="vendor_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone Number'])

    vendors = CustomUser.objects.filter(is_staff=False)

    for vendor in vendors:
        writer.writerow([vendor.name, vendor.email, vendor.phone_number])

    return response
