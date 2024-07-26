from django.contrib import admin
from . import models

@admin.register(models.AttributeName)
class AttributeNameAdmin(admin.ModelAdmin):
    resource_class = models.AttributeName

    list_display = ('id', 'nazev', 'kod', 'zobrazit')
    list_editable = ('zobrazit',)

    list_filter = ("nazev",)
    filter_input_length = {
        "nazev": 3,
    }


@admin.register(models.AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    resource_class = models.AttributeValue

    list_display = ('id', 'hodnota')

    list_filter = ("hodnota",)
    filter_input_length = {
        "hodnota": 3,
    }


admin.site.register(models.Catalog)
admin.site.register(models.Product)
admin.site.register(models.Attribute)
admin.site.register(models.ProductAttribute)
admin.site.register(models.Image)
admin.site.register(models.ProductImage)
# admin.site.register(models.AttributeName)
# admin.site.register(models.AttributeValue)