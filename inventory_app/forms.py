

from django import forms

from inventory_app.models import RawMaterialsStock, Finished_Goods_Stock,Damaged_Goods_Stock,Finished_Goods_Request


class Raw_materials_StockForm(forms.ModelForm):
    class Meta:
        model = RawMaterialsStock
        fields = ['stock']
        widgets = {
            'stock': forms.TextInput(attrs={'class': 'form-control'}),

        }
class Finished_Goods_StockForm(forms.ModelForm):
    class Meta:
        model = Finished_Goods_Stock
        fields = ['stock']
        widgets = {
            'stock': forms.TextInput(attrs={'class': 'form-control'}),

        }

class Damaged_Goods_StockForm(forms.ModelForm):

    class Meta:
        model = Damaged_Goods_Stock
        fields = ['stock']
        widgets = {
            'stock': forms.TextInput(attrs={'class': 'form-control'}),

        }


class Finished_Goods_RequestForm(forms.ModelForm):
    class Meta:
        model = Finished_Goods_Request
        fields = [
            'department',
            'category',
            'name',
            'stock',
            'input_date',
            'remarks',
            'response',

        ]

        widgets = {
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required Quantity'}),
            'input_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Date'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks'}),
            'response': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Reason for Decline', 'style': 'display:none;'}),# Hidden by default

        }