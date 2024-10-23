from django.shortcuts import render,redirect,get_object_or_404
from register_app.models import CustomUser
from hr_app.models import EmployeeDetails
from Glenda_App.models import Menu
from .forms import EmployeeDetailsForm
from django.db.models import Q
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

def AddDetails(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST, request.FILES)  # Added request.FILES for file uploads if needed
        if form.is_valid():
            employee = form.save()
            employee.user_id = id  # Associate the user
            employee.save()
            return redirect('Employee_list')  # Redirect to vendor list after successful submission
    else:
        form = EmployeeDetailsForm()

    return render(request, 'hr/add_employee_details.html', {'form': form, 'menus': menus})

def view_employee_profile(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()

    view = EmployeeDetails.objects.filter(user_id=id)

    return render(request,'hr/view_employee_profile.html',{'view':view,'menus':menus})

def update_employee_details(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()
    view = get_object_or_404(EmployeeDetails, id=id)

    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST,instance=view)

        if form.is_valid():
                form.save()
                return redirect('Employee_list')

    else:
        form = EmployeeDetailsForm(request.POST, instance=view)
    return render(request, 'hr/update_employee_details.html', {'view':view, 'menus': menus,'form':form})

def delete_employee_details(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(EmployeeDetails, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('Employee_list')

    # Render the confirmation page for GET requests
    return render(request, 'hr/delete_employee_details.html', {'dtl': dtl,'menus':menus})


def employee_search(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    # Start with an empty query to show all staff members by default
    employee_list = CustomUser.objects.filter(is_staff=True, is_superuser=False)

    # Check for a search query in the GET request
    search_query = request.GET.get('search_query', '').strip()

    if search_query:
        # Create filters for either phone number or name based on the input
        filters = Q(is_staff=True, is_superuser=False)

        if search_query.isdigit():
            filters &= Q(phone_number__icontains=search_query)  # Filter by phone number if the query is numeric
        else:
            filters &= Q(name__icontains=search_query)  # Filter by name if the query is not numeric

        # Apply filters to employee_list
        employee_list = CustomUser.objects.filter(filters)

    context = {
        'users': employee_list,  # Ensure you pass the filtered list as 'users' to match your template
        'menus': menus,
    }

    return render(request, 'hr/Employee_list.html', context)