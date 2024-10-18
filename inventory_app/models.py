from django.db import models
from production_app.models import damaged_Goods
from production_app.models import water_Finished_Goods
from purchase_app.models import RawMaterials


# Create your models here.

class RawMaterialsStock(models.Model):
    raw_materials = models.ForeignKey(RawMaterials, related_name='stocks', on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(null=True)  # Stock quantity
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.raw_materials.name} - {self.stock} units"


class Finished_Goods_Stock(models.Model):
    finished_goods = models.ForeignKey(water_Finished_Goods, related_name='stocks', on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(null=True)  # Stock quantity
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.finished_goods.name} - {self.stock} units"


class Damaged_Goods_Stock(models.Model):
    damaged = models.ForeignKey(damaged_Goods,related_name='stocks',on_delete=models.CASCADE,null=True)
    stock = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.damaged.name} - {self.stock} units"