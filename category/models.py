from django.db import models
#father models
class CommonInfo(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, null = True) 
    
    class Meta:
        abstract = True

#child models

class Category(CommonInfo):
    def __str__(self):
        return self.category_name 

class Brand(CommonInfo):
    
    def __str__(self):
        return self.category_name 
        
class SELLER(CommonInfo):
    
    def __str__(self):
        return self.category_name 
    

class PRODUCT_BY(CommonInfo):
    
    def __str__(self):
        return self.category_name 
    
class warranty_period(CommonInfo):
    
    def __str__(self):
        return self.category_name 