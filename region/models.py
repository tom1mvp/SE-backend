from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name
    
class Province(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT,  related_name='country',null=False)

    def __str__(self):
        return f'Province name: {self.name} || Country name: {self.country_id.name}'
    
class City(models.Model):
    name = models.CharField(max_length=50, null=False)
    province = models.ForeignKey(Province, on_delete=models.PROTECT,  related_name='provice',null=False)
    
    def __str__(self):
        return f'City name: {self.name} || Province name: {self.province_id.name} || Country name: {self.province_id.country_id.name}'