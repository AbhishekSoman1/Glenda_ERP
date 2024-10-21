
from django.shortcuts import render, redirect, get_object_or_404

from Glenda_App.models import Menu
from purchase_app.forms import CategoryForm, RawMaterialForm

from django.contrib import messages

from purchase_app.models import RawMaterials, RawMaterialCategory
from register_app.models import MenuPermissions


# Create your views here.
def manager_home(request):
    user = request.user

    # Get the user's primary key ID
    user_id = user.id
    # Debug: Print user info
    print(user_id)
    # Get the Menu_permisions instance for the current user
    permissions = MenuPermissions.objects.filter(
        user_id=user_id).first()  # Get the first permission instance for the user

    # Debug: Print permissions

    if permissions:
        # Extract menu IDs from permissions
        menu_ids = permissions.menu_details.values_list('id', flat=True)
        # Filter menus based on permissions
        menus = Menu.objects.filter(id__in=menu_ids).prefetch_related('submenus')
    else:
        # If no permissions are found, return an empty queryset
        menus = Menu.objects.none()

    # Debug: Print filtered menus
    print(f"Filtered Menus: {menus}")
    return render(request,'purchase/home/index.html',{'menus':menus})




def view_rawmaterials(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    view_ca=RawMaterialCategory.objects.all()
    view=RawMaterials.objects.all()
    return render(request,'purchase/view_rawmaterials.html',{'view':view,'view_ca':view_ca,'menus':menus})

def add_category(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print("Request")
        if form.is_valid():
            print("Success")
            form.save()
            messages.success(request, 'Successfull')

            return redirect('view_rawmaterials')
    return render(request, 'purchase/Add_category.html', {'form': form, 'menus': menus})


def create_raw_material(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = RawMaterialForm(request.POST, request.FILES)  # Use request.FILES for file upload
        if form.is_valid():
            form.save()
            return redirect('view_rawmaterials')  # Redirect to a list view or another page after saving
    else:
        form = RawMaterialForm()

    return render(request, 'purchase/add_rawmaterials.html', {'form': form, 'menus': menus})

def update_rawmaterials(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(RawMaterials, id=id)

    if request.method == 'POST':
        form = RawMaterialForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_rawmaterials')  # Redirect to the list view or any relevant view
    else:
        form = RawMaterialForm(instance=mem)

    return render(request, 'purchase/update_rawmaterials.html', {'form': form, 'menus': menus})


def delete_rawmaterils(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(RawMaterials, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_rawmaterials')

    # Render the confirmation page for GET requests
    return render(request, 'purchase/delete_rawmaterials.html', {'dtl': dtl,'menus':menus})
