from django.contrib import admin
from rangefilter.filters import (
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder
)

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


@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    resource_class = models.Attribute
    list_display = ('id', 'nazev_atributu_id', 'hodnota_atributu_id')
    list_filter = (
        'nazev_atributu_id', 
        'hodnota_atributu_id'
    )
    filter_input_length = {
        'nazev_atributu_id': 3, 
        'hodnota_atributu_id': 2
    }


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    resource_class = models.Image
    list_display = ('id', 'obrazek')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    resource_class = models.Product
    list_display = ('id', 'nazev', 'description', 
    'cena', 'mena', 'published_on', 'is_published')
    list_editable = ('is_published', 'published_on')
    list_filter = (
        'nazev', 'mena', 
        ('cena', NumericRangeFilterBuilder()), 
        ('published_on', DateTimeRangeFilterBuilder())
    )
    filter_input_length = {
        'nazev': 3, 
    }


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    resource_class = models.ProductImage
    list_display = ('id', 'product', 'obrazek_id', 'nazev')
    list_filter = ('nazev',)
    filter_input_length = {
        'nazev': 3, 
    }


@admin.register(models.ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    resource_class = models.ProductAttributes
    list_display = ('id', 'attribute', 'product')
    list_filter = ('attribute', 'product')
    filter_input_length = {
        'attribute': 3, 
        'product': 3
    }


@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    resource_class = models.Catalog
    list_display = ('id', 'nazev', 'obrazek_id')
    raw_id_fields  = ('products_ids', 'attributes_ids')
    list_filter = ('nazev',)
    filter_input_length = {
        'nazev': 3, 
    }