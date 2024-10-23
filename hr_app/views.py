from django.shortcuts import render,redirect
from register_app.models import CustomUser
from hr_app.models import EmployeeDetails
from Glenda_App.models import Menu
from .forms import EmployeeDetailsForm

def Employee_list(request):
    # Fetch all users with is_staff=True
    users = CustomUser.objects.filter(is_staff=True,is_superuser=False)

    # Filter EmployeeDetails where the user is in the hr_users queryset

    # Load the menus (assuming this is required elsewhere in your template)
    menus = Menu.objects.prefetch_related('submenus').all()

    # Pass the filtered HR employee details and menus to the context
    context = {
        'menus': menus,
        'users':users
    }

    return render(request, 'hr/Employee_list.html', context)

def AddDetails(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST, request.FILES)  # Added request.FILES for file uploads if needed
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user_id = id  # Associate the user
            employee.save()
            form.save_m2m()  # Save the many-to-many field for materials
            return redirect('Employee_list')  # Redirect to vendor list after successful submission
    else:
        form = EmployeeDetailsForm()

    return render(request, 'hr/add_employee_details.html', {'form': form, 'menus': menus})