from django.contrib import admin
from accounts.models import Account


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'acc_type',
        'data_joined',
        'is_active',
        'first_name',
        'last_name',
        'store',
        'phone',
        'address'
        )
    fields = ('id','username','acc_type','is_active','is_admin',)
    list_filter = ('data_joined','is_active','acc_type')
    search_fields = ['username','first_name','last_name']
    ordering = ('username','data_joined','acc_type')
    readonly_fields = ('id','username','data_joined','store','first_name','password','phone','address','last_name','email')
    filter_horizontal = ()


admin.site.register(Account,UsersAdmin)