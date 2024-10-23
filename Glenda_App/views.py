from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from Glenda_App.forms import MenuForm, SubMenuForm
from Glenda_App.models import Menu
from inventory_app.models import Finished_Goods_Stock, RawMaterialsStock
from production_app.models import water_Finished_Goods, damaged_Goods
from purchase_app.models import RawMaterials
from vendor_app.models import vendor_register
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    # Fetch menus and counts
    menus = Menu.objects.prefetch_related('submenus').all()
    vendor=vendor_register.objects.all()

    vendor_count = vendor_register.objects.count()
    goods = water_Finished_Goods.objects.count()
    da = damaged_Goods.objects.count()
    raw_materials = RawMaterials.objects.all()
    la = [material.name for material in raw_materials]
    tt = [material.total_stock for material in raw_materials]
    # Get today's date
    today = timezone.now().date()

    # Define the last 7 days for the line chart
    dates = [today - timedelta(days=i) for i in range(7)]

    # Fetch finished goods stock data for the last 7 days
    daily_stock_summary = Finished_Goods_Stock.objects.filter(date__gte=today - timedelta(days=6)).values(
        'date').annotate(total_stock=Sum('stock')).order_by('date')

    # Prepare data for the chart
    labels = []
    data = []

    # Fill the labels and data with zeros for days without stock entries
    for date in dates:
        total_stock = 0
        for entry in daily_stock_summary:
            if entry['date'] == date:
                total_stock = entry['total_stock'] or 0
                break
        labels.append(date.strftime('%Y-%m-%d'))  # Format date as needed
        data.append(total_stock)  # Use total stock or 0 if no entry

    # Prepare the context for rendering
    context = {
        'menus': menus,
        'vendor': vendor_count,
        'goods': goods,
        'da': da,
        'ven':vendor,
        'labels':la,
        'data':tt,
        'chart_data': {
            'labels': labels,
            'data': data,
        },
    }

    return render(request, 'index.html', context)
from django.http import JsonResponse

def raw_materials_data(request):
    raw_materials = RawMaterials.objects.all()
    data = [
        {
            'name': material.name,
            'total_stock': material.total_stock
        }
        for material in raw_materials
    ]
    return JsonResponse(data, safe=False)

def calendar(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    return render(request, 'calendar.html', {'menus': menus})

def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Change to redirect to index after creation
    else:
        form = MenuForm()
    return render(request, 'create_menu.html', {'form': form})

def create_submenu(request):
    if request.method == 'POST':
        form = SubMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Change to redirect to index after creation
    else:
        form = SubMenuForm()
    return render(request, 'create_submenu.html', {'form': form})


# views.py
# import matplotlib.pyplot as plt
# from io import BytesIO
# from django.http import HttpResponse
# from purchase_app.models import RawMaterials
# from inventory_app.models import Finished_Goods_Stock
#
# def pie_chart_view(request):
#     # Example: Fetch raw materials and stock data from the database
#     raw_materials = RawMaterials.objects.all()
#     names = [material.name for material in raw_materials]
#     stocks = [material.total_stock for material in raw_materials]
#
#     # Generate the pie chart
#     plt.figure(figsize=(7, 7))
#     plt.pie(stocks, labels=names, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
#     plt.title('Raw Materials Stock Distribution')
#     plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
#
#     # Save the plot to a BytesIO object
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     plt.close()
#
#     # Return the image as an HTTP response
#     buffer.seek(0)
#     return HttpResponse(buffer, content_type='image/png')
#
# from io import BytesIO
# import base64
#

# def daily_stock_bar_chart_image(request):
# #     # Get stock data ordered by date
# #     stock_data = Finished_Goods_Stock.objects.all().order_by('date')
# #
# #     # Get unique dates and corresponding stock values
# #     dates = [stock.date for stock in stock_data]
# #     stock_values = [stock.stock for stock in stock_data]
# #
# #     # Create the bar chart
# #     plt.figure(figsize=(10, 6))
# #     plt.bar(dates, stock_values, color='blue')
# #
# #     # Add labels and title
# #     plt.xlabel('Date')
# #     plt.ylabel('Stock Quantity')
# #     plt.title('Daily Water Stock')
# #
# #     # Convert the plot to an image
# #     buffer = BytesIO()
# #     plt.savefig(buffer, format='png')
# #     buffer.seek(0)
# #     plt.close()
# #
# #     # Return the image as an HTTP response
# #     return HttpResponse(buffer, content_type='image/png')


# def stock_data(request):
#     # Query data
#     finished_goods = water_Finished_Goods.objects.all()
#     raw_materials = RawMaterialsStock.objects.all()
#
#     # Prepare data
#     finished_goods_data = {
#         "names": [item.name for item in finished_goods],
#         "stock": [item.total_stock for item in finished_goods],
#     }
#
#     raw_materials_data = {
#         "names": [item.raw_materials.name for item in raw_materials],
#         "stock": [item.stock for item in raw_materials],
#     }
#
#     return JsonResponse({
#         "finished_goods": finished_goods_data,
#         "raw_materials": raw_materials_data,
#     })


