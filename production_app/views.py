from django.shortcuts import render, redirect, get_object_or_404

from Glenda_App.models import Menu
from production_app.forms import water_category_Form, finishedwaterForm, damaged_goods_Form,DamagedForm,update_damaged_goods_Form
from django.contrib import messages
from django.db.models import Q
from production_app.models import water_Finished_goods_category, water_Finished_Goods, damaged_Goods,Damaged_good_category
from inventory_app.models import Finished_Goods_Request
from inventory_app.forms import Finished_Goods_RequestForm


# Create your views here.

def view_finished_water_good(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    cc=water_Finished_goods_category.objects.all()
    view_ca=water_Finished_Goods.objects.all()

    return render(request,'production/view_finished_goods.html',{'view_ca':view_ca,'cc':cc,'menus':menus})

def addwater_category(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    form = water_category_Form()
    if request.method == 'POST':
        form = water_category_Form(request.POST)
        print("Request")
        if form.is_valid():
            print("Success")
            form.save()
            messages.success(request, 'Successfull')

            return redirect('add_category')
    return render(request,'production/create_water_category.html',{'form':form,'menus':menus})



def create_water(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = finishedwaterForm(request.POST, request.FILES)  # Ensure request.FILES is used for image upload
        if form.is_valid():
            form.save()
            return redirect('view_finished_water_good')  # Replace with the correct URL or view name
    else:
        form = finishedwaterForm()

    return render(request, 'production/create_water.html', {'form': form, 'menus': menus})

def update_finished_goods(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(water_Finished_Goods, id=id)

    if request.method == 'POST':
        form = finishedwaterForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_finished_water_good')  # Redirect to the list view or any relevant view
    else:
        form = finishedwaterForm(instance=mem)

    return render(request, 'production/update_water.html', {'form': form,'menus':menus})


def delete_goods(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(water_Finished_Goods, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_finished_water_good')

    # Render the confirmation page for GET requests
    return render(request, 'production/delete_water.html', {'dtl': dtl,'menus':menus})



def add_damaged_good_category(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    if request.method == "POST":
        form = DamagedForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Successfull')

            return redirect('add_category')
        else:
            return render(request,'production/damaged_good_category.html',{'form':form, 'menus':menus})
    else:
        form = DamagedForm(request.POST)
        return render(request, 'production/damaged_good_category.html', {'form': form,  'menus':menus})
def damaged_goods(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    dd=damaged_Goods.objects.all()
    return render(request, 'production/damaged_goods.html', {'menus': menus,'dd':dd})


def Add_damagedgoods(request):
    menus = Menu.objects.prefetch_related('submenus').all()

    if request.method == 'POST':
        form = damaged_goods_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('damaged_goods')  # Replace 'Route' with the actual view name or URL pattern
    else:
        form = damaged_goods_Form()

    return render(request, 'production/add_damaged_goods.html', {'form': form, 'menus': menus})

def damage_delete(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()
    details = get_object_or_404(damaged_Goods,id=id)

    if request.method == 'POST':
        try:
            details.delete()
            return redirect('damaged_goods')
        except Exception as e:
            print(e)
    return render(request,'production/damage_delete.html',{'menus':menus})

def update_damage(request,id):
    menus = Menu.objects.prefetch_related('submenus').all()
    details = get_object_or_404(damaged_Goods, id=id)

    if request.method == 'POST':
        form = update_damaged_goods_Form(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('damaged_goods')

    else:
        form = update_damaged_goods_Form(instance=details)
    return render(request,'production/update_damage.html',{'menus':menus,'form':form})



def request_messages(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    data = Finished_Goods_Request.objects.all()

    return render(request,'production/production_request_messages.html',{'data':data,'menus':menus})


def request_messages_detail(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    # Fetch the specific request by its primary key (id)
    request_data = get_object_or_404(Finished_Goods_Request, pk=id)

    if request.method == 'POST':
        # Check if "Accept" button was clicked
        if 'accept' in request.POST:
            # Update status to 'completed'
            request_data.status = 'completed'
            request_data.save()
            return redirect('request_messages')

        # Check if "Decline" button was clicked
        elif 'decline' in request.POST:
            # Get the response from the POST data
            response = request.POST.get('response', '').strip()

            if response:
                # Update the response and status if the response is provided
                request_data.response = response
                request_data.status = 'declined'
                request_data.save()
                return redirect('request_messages')
            else:
                # If no response is provided, show an error message
                error_message = "Please provide a reason for declining."
                return render(request, 'production/production_request_messages_in_detail.html', {
                    'data': request_data,
                    'menus': menus,
                    'error_message': error_message
                })

    # Render the page with the form and request data
    return render(request, 'production/production_request_messages_in_detail.html', {
        'data': request_data,
        'menus': menus
    })

def search(request):
    # Fetch all categories
    categories = Damaged_good_category.objects.all()

    # Initialize the queryset for damaged goods
    damaged_goods_list = damaged_Goods.objects.all()
    menus = Menu.objects.prefetch_related('submenus').all()

    # Handle search requests
    if request.method == 'GET':
        damaged_name = request.GET.get('name', None)
        damaged_category = request.GET.get('category', None)

        # Build filters
        filters = Q()

        # If the search name is provided, filter by the name in damaged_Goods
        if damaged_name:
            filters &= Q(name__icontains=damaged_name)

        # If a valid category is selected, filter by the category
        if damaged_category:
            filters &= Q(category_id=damaged_category)  # Use category_id to filter

        # Apply the filters to the queryset if filters are provided
        if filters:
            damaged_goods_list = damaged_Goods.objects.filter(filters)

    # Prepare context with the filtered or full list of damaged goods
    context = {
        'dd': damaged_goods_list,  # This is the queryset for the table in the HTML
        'categories': categories,
        'menus':menus
    }

    return render(request, 'production/damaged_goods.html', context)

