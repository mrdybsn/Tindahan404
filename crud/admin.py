from django.contrib import admin
from django import forms
from .models import (User, Category, Product, Sale, SaleItem, Supplier, Purchase, PurchaseItem)

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'password': forms.PasswordInput(attrs={'class': 'border rounded p-2 w-full'}),
            'role': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'contact_number': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'address': forms.Textarea(attrs={'class': 'border rounded p-2 w-full'}),
            'gender': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'birth_date': forms.DateInput(attrs={'class': 'border rounded p-2 w-full', 'type': 'date'}),
        }

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('username', 'role', 'contact_number', 'email')
    search_fields = ('username', 'email', 'contact_number')
    list_filter = ('role', 'gender')
    ordering = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.site_header = "Tindahan404"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome Back, Admin!"