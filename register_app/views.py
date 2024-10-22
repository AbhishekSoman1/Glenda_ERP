from Glenda_App.models import Menu
from register_app.forms import CustomUserForm, CustomLoginForm, designation_Form, department_Form, Permission_Form

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth import login,logout

from register_app.models import CustomUser, designation


def register_view(request):
    # Fetching menus and their related submenus for display
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Set is_staff to True
            user.save()  # Save the user instance

            # Log the user in after successful registration
            messages.success(request, "Registration successful!")
            return redirect('view_users')

        messages.error(request, "Please correct the errors below.")

    else:
        # Create an empty form for a GET request
        form = CustomUserForm()

    # Render the registration page with the form and menus
    return render(request, 'register/create_user.html', {'form': form, 'menus': menus})


def Edit_user(request, id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('view_users')  # Redirect to a relevant page (e.g., user list or dashboard)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'register/update_users.html', {'form': form, 'user': user})


def delete_user_view(request, user_id):
    # Retrieve the user object to be deleted
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        # If confirmed, delete the user
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('view_users')  # Redirect to a list of users or homepage

    # If request is GET, prompt confirmation
    return render(request, 'register/delete_user.html', {'user': user})



# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Redirect based on user role
#                 if user.is_superuser:
#                     return redirect('admin_home')  # Redirect to admin dashboard for superusers
#                 department_name = user.department.dept_Name if user.department else None
#                 designation_name = user.designation.user_type if user.designation else None
#
#                 # Redirect based on department and designation
#                 if designation_name == 'Executive' and department_name == 'Sales':
#                     return redirect('sales_home')
#                 elif designation_name == 'Manager' and department_name == 'Sales':
#                     return redirect('vender_home')
#                 elif designation_name == 'Assistant Manager' and department_name == 'Purchase':
#                     return redirect('manager_home')
#                 elif designation_name == 'Executive' and department_name == 'Logistics':
#                     return redirect('manager_home')
#                 else:
#                     return redirect('default_dashboard')  # Default page for other users
#     else:
#         form = CustomLoginForm()
#
#     return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., home page)
    return redirect(reverse('mainindex'))


def add_department(request):
    if request.method == 'POST':
        form = department_Form(request.POST)  # Use request.FILES for file upload
        if form.is_valid():
            form.save()
            return redirect('adddepartment')  # Redirect to a list view or another page after saving
    else:
        form = department_Form()

    return render(request, 'register/create_department.html', {'form': form})


def add_designation(request):
    if request.method == 'POST':
        form = designation_Form(request.POST)  # Use request.FILES for file upload
        if form.is_valid():
            form.save()
            return redirect('add_designation')  # Redirect to a list view or another page after saving
    else:
        form = designation_Form()

    return render(request, 'register/create_designation.html', {'form': form})


def view_users(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    view = CustomUser.objects.filter(is_superuser=False, is_staff=True)

    return render(request, 'register/view_users.html', {'view': view, 'menus': menus})


def create_permission(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = Permission_Form(request.POST)
        if form.is_valid():
            permission = form.save(commit=False)
            permission.user_id =id  # Associate the current user
            permission.save()
            form.save_m2m()  # Save many-to-many data for the form
            return redirect('view_users')  # Redirect to a success page or list view
    else:
        form = Permission_Form()
    return render(request, 'register/add_permissions.html', {'form': form,'menus':menus})


from django.http import JsonResponse

def load_designations(request):
    department_id = request.GET.get('department_id')
    designations = designation.objects.filter(dept_id=department_id).values('id', 'user_type')  # Adjust field names as necessary
    return JsonResponse(list(designations), safe=False)


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user role
                if user.is_superuser:
                    return redirect('admin_home')  # Redirect to admin dashboard for superusers

                department_name = user.department.dept_Name if user.department else None
                designation_name = user.designation.user_type if user.designation else None

                # Redirect based on department and designation
                if designation_name == 'Executive' and department_name == 'Sales':
                    return redirect('sales_home')
                elif designation_name == 'Manager' and department_name == 'Sales':
                    return redirect('vender_home')
                elif designation_name == 'Assistant Manager' and department_name == 'Purchase':
                    return redirect('manager_home')
                elif designation_name == 'Executive' and department_name == 'Logistics':
                    return redirect('executive_logistics_dashboard')
                else:
                    return redirect('default_dashboard')  # Default page for other users
            else:
                # Add an error to the form if authentication fails
                form.add_error(None, "Invalid email or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., home page)
    return redirect(reverse('admin'))
