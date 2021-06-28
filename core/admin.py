from django.contrib import admin

# Register your models here.
from .models import Product , Category,Top_banner,Deal
admin.site.register(Top_banner)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id','name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id','name','slug','price','available','updated')
	list_filter = ('available','created','updated')
	list_editable = ('price','available',)
	prepopulated_fields = {'slug':('name',)}

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
	list_display = ('product_id','off_percentage','updated')
	list_editable = ('off_percentage',)

