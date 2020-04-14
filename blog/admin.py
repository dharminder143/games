from django.contrib import admin
from . models import Product,category
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProductAdmin(ImportExportModelAdmin):
	list_display=('category','gamename','vendor','GameURL','IMGURL')

class categoryAdmin(ImportExportModelAdmin):
	pass

admin.site.register(Product,ProductAdmin)
admin.site.register(category,categoryAdmin)
