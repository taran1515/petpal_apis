from django.contrib import admin
from product.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(CancelOrder)
admin.site.register(Post)
admin.site.register(Order_item)
admin.site.register(Order_item_meta)
admin.site.register(Petpal_User)

@admin.register(Medicine)
class ViewAdmin(ImportExportModelAdmin):
    pass
