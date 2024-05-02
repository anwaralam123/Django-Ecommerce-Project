from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# # Create your models here.
class ProductCategory(models.Model):
    category_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

class Company(models.Model):
    product_category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE,default=None)
    company_name=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name 

class Product(models.Model):
    product_category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE,default=None)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100,default=None)
    short_desc=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics', default=None)
    item_desc=models.CharField(max_length=100)
    discount=models.IntegerField()
    price=models.FloatField()
    discount_price=models.FloatField()
    trending_items=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='pics')

class ProductDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    memory=models.CharField(max_length=100)
    warranty=models.IntegerField()
    Available_Choices=(
        ('In stock','In stock'),
        ('Out stock','Out stock'),
    )
    availability=models.CharField(max_length=70, choices=Available_Choices)
    description=models.TextField()
    def __str__(self):
        return self.product.product_name

class ProductDescription(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    heading=models.CharField(max_length=100)
    imgs=models.ImageField(upload_to='pics')
    description=models.TextField()

class AdditionalInformation(models.Model):
    additional_info=models.ForeignKey("main.AdditionalInformation",on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    feature_name=models.CharField(max_length=200)
    feature_description=models.TextField()

    def __str__(self):
        return f"{self.feature_name}-{self.product.product_name}"
    

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default=None)
    title=models.CharField(max_length=200)
    review=models.TextField()
    rate=models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ])
    created_at=models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_detail=models.ForeignKey(ProductDetail,on_delete=models.CASCADE,null=True,blank=True)
    product_qty=models.PositiveIntegerField(default=1,null=True,blank=False)
    total_amount=models.FloatField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    # def total_price(self):
    #     price=((self.product_qty)*(self.product.discount_price))
    #     return price

class Cart_Total(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sub_total=models.DecimalField(max_digits = 10, decimal_places=2,null=True,blank=True)
    total=models.DecimalField(max_digits = 10, decimal_places=2,null=True,blank=True) 


class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    area_code=models.CharField(max_length=100)
    primary_phone=models.CharField(max_length=100)
    street_address=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=100)
    business_address=models.BooleanField(default=False)