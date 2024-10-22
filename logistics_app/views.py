from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from Glenda_App.models import Menu
from logistics_app.forms import DriverForm,VehicleForm, RouteForm, RoutePlanForm
from logistics_app.models import Driver, Route, Route_Plan, Vehicle


# Create your views here.

def Add_driver(request):
    menus = Menu.objects.all()

    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Add_driver')
    else:
        form = DriverForm()
        return render(request, 'logistics/add_driver.html', {'form': form, 'menus': menus})


def view_driver(request):
    menus = Menu.objects.all()
    dr = Driver.objects.all()
    return render(request, 'logistics/view_driver.html', {'menus': menus, 'dr': dr})


def update_driver(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(Driver, id=id)

    if request.method == 'POST':
        form = DriverForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_driver')  # Redirect to the list view or any relevant view
    else:
        form = DriverForm(instance=mem)

    return render(request, 'logistics/update_driver.html', {'form': form, 'menus': menus})


def delete_driver(request, id):
    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(Driver, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_driver')

    # Render the confirmation page for GET requests
    return render(request, 'logistics/delete_driver.html', {'dtl': dtl})


def Add_vehicle(request):
    menus = Menu.objects.all()

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_vehicle')
    else:
        form = VehicleForm()
        return render(request, 'logistics/add_vehicle.html', {'form': form, 'menus': menus})


def view_vehicle(request):
    menus = Menu.objects.all()
    dr = Vehicle.objects.all()
    return render(request, 'logistics/view_vehicle.html', {'menus': menus, 'dr': dr})


def update_vehicle(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(Vehicle, id=id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_vehicle')  # Redirect to the list view or any relevant view
    else:
        form = VehicleForm(instance=mem)

    return render(request, 'logistics/update_vehicle.html', {'form': form, 'menus': menus})


def delete_vehicle(request, id):
    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(Vehicle, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_vehicle')

    # Render the confirmation page for GET requests
    return render(request, 'logistics/delete_vehicle.html', {'dtl': dtl})


from django.shortcuts import render
from .models import Route

def create_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_route')
    else:
        form = RouteForm()

    return render(request, 'logistics/add_route.html', {'form': form})

from django.http import JsonResponse

def get_route_details(request):
    route_id = request.GET.get('route_id')

    if route_id:
        # Attempt to fetch the route object
        route = get_object_or_404(Route, id=route_id)  # Use get_object_or_404 for cleaner error handling

        data = {
            'total_distance': route.total_distance,  # Field from Route model
            'starting_point': route.starting_point,  # Field from Route model
            'ending_point': route.ending_point,  # Field from Route model
        }
        return JsonResponse(data)

    return JsonResponse({'error': 'No route ID provided'}, status=400)



def view_route(request):
    menus = Menu.objects.all()
    dr = Route.objects.all()
    return render(request, 'logistics/view_route.html', {'menus': menus, 'dr': dr})


def update_route(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(Route, id=id)

    if request.method == 'POST':
        form = RouteForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_route')  # Redirect to the list view or any relevant view
    else:
        form = RouteForm(instance=mem)

    return render(request, 'logistics/update_route.html', {'form': form, 'menus': menus})


def delete_route(request, id):
    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(Route, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_route')

    # Render the confirmation page for GET requests
    return render(request, 'logistics/delete_route.html', {'dtl': dtl})


def Add_routeplan(request):
    menus = Menu.objects.all()

    if request.method == 'POST':
        form = RoutePlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_routeplan')
    else:
        form = RoutePlanForm()
        return render(request, 'logistics/add_routeplan.html', {'form': form, 'menus': menus})


def view_routeplan(request):
    menus = Menu.objects.all()
    dr = Route_Plan.objects.all()
    return render(request, 'logistics/view_routeplan.html', {'menus': menus, 'dr': dr})


def update_routeplan(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()

    mem = get_object_or_404(Route_Plan, id=id)

    if request.method == 'POST':
        form = RoutePlanForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('view_routeplan')  # Redirect to the list view or any relevant view
    else:
        form = RoutePlanForm(instance=mem)

    return render(request, 'logistics/update_routeplan.html', {'form': form, 'menus': menus})


def delete_routeplan(request, id):
    # Fetch the object or return a 404 error if not found
    dtl = get_object_or_404(Route_Plan, id=id)

    if request.method == "POST":
        dtl.delete()
        return redirect('view_routeplan')

    # Render the confirmation page for GET requests
    return render(request, 'logistics/delete_routeplan.html', {'dtl': dtl})


from django.shortcuts import render

# Create your views here.
