

from django import forms

from inventory_app.models import RawMaterialsStock, Finished_Goods_Stock,Damaged_Goods_Stock


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