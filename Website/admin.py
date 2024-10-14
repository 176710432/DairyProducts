from django.contrib import admin
from .models import Cart,Product,Customer,Payment,OrderPlaced,Wishlist

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image']
    search_fields = ['title', 'category']  # Enables search by title and category
    list_filter = ['category']  # Enables filtering by category
    ordering = ['id']  # Default ordering by id
    prepopulated_fields = {'title': ('title',)}  # Automatically fills the slug field based on title (if you have a slug field)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'locality', 'city', 'state', 'zipcode']
    search_fields = ['name', 'city']  # Enables search by name and city
    list_filter = ['state']  # Enables filtering by state
    ordering = ['id']  # Default ordering by id

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product']