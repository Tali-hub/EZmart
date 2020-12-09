from django.contrib import admin

# Register your models here.
from products.models import Product,Regulation



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'quantity',
        'category',
        'active',
        'time_stamp',
        )
    list_filter = ('title','category','active')
    search_fields = ['title','description','last_name']
    ordering = ('title','active',)
    fields = ('id','title','category','description',)
    readonly_fields = ('id','active','price','quantity','store',)
    filter_horizontal = ()
admin.site.register(Product,ProductAdmin)
class RegulationAdmin(admin.ModelAdmin):
    list_display = (
        'last_changed',
        )
    ordering = ('last_changed',)
    filter_horizontal = ()
admin.site.register(Regulation,RegulationAdmin)