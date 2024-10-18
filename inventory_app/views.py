from django.shortcuts import render, get_object_or_404, redirect

from Glenda_App.models import Menu
from inventory_app.forms import Raw_materials_StockForm, Finished_Goods_StockForm,Damaged_Goods_StockForm
from inventory_app.models import RawMaterialsStock
from production_app.models import water_Finished_Goods,damaged_Goods
from purchase_app.models import RawMaterials

from django.db.models import Sum

# Create your views here.




def raw_materials_view(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    raw_materials = RawMaterials.objects.prefetch_related('stocks').all()

    # Calculate total stock for each raw material
    total_stocks = {
        material.id: material.stocks.aggregate(total=Sum('stock'))['total'] or 0
        for material in raw_materials
    }

    return render(request, 'inventory/view_raw_materials.html', {'view': raw_materials, 'menus': menus, 'total_stocks': total_stocks})

def update_stocks(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()
    raw_material = get_object_or_404(RawMaterials, id=id)

    if request.method == 'POST':
        form = Raw_materials_StockForm(request.POST)
        if form.is_valid():
            stock_entry = form.save(commit=False)
            stock_entry.raw_materials = raw_material  # Set the raw material
            stock_entry.save()  # Save the new stock entry

            # Update the total stock for the raw material
            total_stock = raw_material.stocks.aggregate(total=Sum('stock'))['total'] or 0
            raw_material.total_stock = total_stock
            raw_material.save()  # Save the updated total stock

            return redirect('Raw_materials_view')  # Redirect to the list view
    else:
        form = Raw_materials_StockForm()

    return render(request, 'inventory/add_stock.html', {
        'form': form,
        'menus': menus,
        'raw_material': raw_material
    })




def update_finished_goods_stocks(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()
    finished_goods = get_object_or_404(water_Finished_Goods, id=id)

    if request.method == 'POST':
        form = Finished_Goods_StockForm(request.POST)
        if form.is_valid():
            stock_entry = form.save(commit=False)
            stock_entry.finished_goods = finished_goods  # Set the raw material
            stock_entry.save()  # Save the new stock entry

            # Update the total stock for the raw material
            total_stock = finished_goods.stocks.aggregate(total=Sum('stock'))['total'] or 0
            finished_goods.total_stock = total_stock
            finished_goods.save()  # Save the updated total stock

            return redirect('finishedgoods_stock_view')  # Redirect to the list view
    else:
        form = Finished_Goods_StockForm()

    return render(request, 'inventory/add_finishedgoods_stock.html', {
        'form': form,
        'menus': menus,
        'finished_goods': finished_goods
    })


def finishedgoods_stock_view(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    finished_goods = water_Finished_Goods.objects.prefetch_related('stocks').all()

    # Calculate total stock for each raw material
    total_stocks = {
        material.id: material.stocks.aggregate(total=Sum('stock'))['total'] or 0
        for material in finished_goods
    }

    return render(request, 'inventory/view_finished_goods.html', {'view': finished_goods, 'menus': menus, 'total_stocks': total_stocks})

def update_damaged_goods_stocks(request, id):
    menus = Menu.objects.prefetch_related('submenus').all()
    damaged_goods = get_object_or_404(damaged_Goods, id=id)

    if request.method == 'POST':
        form = Finished_Goods_StockForm(request.POST)
        if form.is_valid():
            stock_entry = form.save(commit=False)
            stock_entry.damaged_goods = damaged_goods  # Set the raw material
            stock_entry.save()  # Save the new stock entry

            # Update the total stock for the raw material
            total_stock = damaged_goods.stocks.aggregate(total=Sum('stock'))['total'] or 0
            damaged_goods.total_stock = total_stock
            damaged_goods.save()  # Save the updated total stock

            return redirect('damagedgoods_stock_view')  # Redirect to the list view
    else:
        form = Finished_Goods_StockForm()

    return render(request, 'inventory/add_damage_stock.html', {
        'form': form,
        'menus': menus,
        'damaged_goods': damaged_goods
    })


def damagedgoods_stock_view(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    damaged_goods = damaged_Goods.objects.prefetch_related('stocks').all()

    # Calculate total stock for each raw material
    total_stocks = {
        material.id: material.stocks.aggregate(total=Sum('stock'))['total'] or 0
        for material in damaged_goods
    }

    return render(request, 'inventory/view_damaged_goods.html', {'view': damaged_goods, 'menus': menus, 'total_stocks': total_stocks})