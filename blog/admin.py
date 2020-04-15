from django.contrib import admin
from . models import Product
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProductAdmin(ImportExportModelAdmin):
	list_display=('category','gamename','vendor','GameURL','IMGURL')

admin.site.register(Product,ProductAdmin)
