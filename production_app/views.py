from django.shortcuts import render, redirect, get_object_or_404

from Glenda_App.models import Menu
from production_app.forms import water_category_Form, finishedwaterForm, damaged_goods_Form,DamagedForm,update_damaged_goods_Form
from django.contrib import messages

from production_app.models import water_Finished_goods_category, water_Finished_Goods, damaged_Goods,Damaged_good_category


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
            return render(request,'production/damaged_good_category.html',{'form':form, menus:'menus'})
    else:
        form = DamagedForm(request.POST)
        return render(request, 'production/damaged_good_category.html', {'form': form, menus: 'menus'})
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
    return render(request,'production/damage_delete.html',{menus:'menus'})

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
    return render(request,'production/update_damage.html',{details:'details',menus:'menus','form':form})