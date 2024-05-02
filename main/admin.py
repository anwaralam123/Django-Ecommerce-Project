from django.contrib import admin
from .models import Company,ProductCategory,Product,Image,ProductDetail,ProductDescription,AdditionalInformation,Rating,Cart,Cart_Total,ShippingAddress
# admin.site.register(Company)
# admin.site.register(ProductCategory)
# admin.site.register(Product)
# admin.site.register(Image)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','product','image']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','product_category','company_name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_category','company','product_name','trending_items']


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin): 
    list_display=['id','product','color','code','memory','warranty','availability','description']


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display=['id','heading','imgs','description']

@admin.register(AdditionalInformation)
class AdditionalInformationAdmin(admin.ModelAdmin):
    list_display=['id','feature_name','feature_description','additional_info']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=['id','name','title','review','rate','created_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','product_qty','total_amount','created_at']


@admin.register(Cart_Total)
class CartTotalAdmin(admin.ModelAdmin):
    list_display=['id','user','sub_total','total']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','company_name','area_code','primary_phone','street_address','zip_code','business_address']




# @admin.register(Product)
# # Register your models here.
# class productAdmin(admin.ModelAdmin):
#     list_display=['id','productname','productdesc','shortdesc','image','discount','price','discountprice']

# @admin.register(Tablet)
# # Register your models here.
# class TabletAdmin(admin.ModelAdmin):
#     list_display=['id','productname','productdesc','shortdesc','image','discount','price','discountprice']