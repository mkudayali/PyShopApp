from .models import Product, ProCategory, SampleMultipleImgProduct, ProductMain, ProductMainImgs
from django.contrib import admin
from .forms import ProductMainAdminForm


class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'stock', 'category_name', 'gender')


class ProCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdminInLine(admin.TabularInline):
    model = ProductMainImgs


@admin.register(ProductMain)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'categoryName', 'gender')
    form = ProductMainAdminForm
    inlines = [ProductAdminInLine]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProCategory, ProCategoryAdmin)