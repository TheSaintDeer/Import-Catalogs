from django.db import models
from django.core.validators import RegexValidator


class AttributeName(models.Model):
    '''Attribute name'''
    nazev = models.CharField(
        max_length=100
    )
    kod = models.CharField(
        max_length=100, 
        blank=True
    )
    zobrazit = models.BooleanField(
        default=False
    )    

    def __str__(self) -> str:
        return f'{self.nazev}'


class AttributeValue(models.Model):
    '''Attribute value'''
    hodnota = models.CharField(
        max_length=100
    )

    def __str__(self) -> str:
        return f'{self.hodnota}'


class Attribute(models.Model):
    '''An attribute containing a name and a value'''
    nazev_atributu_id = models.ForeignKey(
        'AttributeName',
        on_delete=models.CASCADE
    )
    hodnota_atributu_id = models.ForeignKey(
        'AttributeValue',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.nazev_atributu_id.nazev}: {self.hodnota_atributu_id.hodnota}'


class Product(models.Model):
    '''Product provided in certain catalogs'''
    nazev = models.CharField(
        max_length=100
    )
    description = models.TextField()
    cena = models.FloatField()
    mena = models.CharField(
        max_length=3
    )
    published_on = models.DateTimeField(
        blank=True,
        null=True
    )
    is_published = models.BooleanField(
        default=False,
    )
    attributes = models.ManyToManyField(
        'Attribute',
        through='ProductAttributes'
    )
    images = models.ManyToManyField(
        'Image',
        through='ProductImage'
    )

    def __str__(self) -> str:
        return f'{self.nazev}'


class ProductAttributes(models.Model):
    '''Model for many-to-many relationship between Product and Attribute tables'''
    attribute = models.ForeignKey(
        'Attribute',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )


class Image(models.Model):
    '''Model for storing a reference to an image'''
    obrazek = models.URLField(
        validators=[
            RegexValidator(
                #the link must start with 'https://' and end with '.jpg' and contain at least one character
                regex=r'^https:\/\/.+\.jpg$', 
                message="Please enter a valid image link.",
                code="invalid_link",
            ),
        ],
    )

    def __str__(self) -> str:
        return f'{self.obrazek}'


class ProductImage(models.Model):
    '''Model for many-to-many relationship between Product and Image tables'''
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    obrazek_id = models.ForeignKey(
        'Image',
        on_delete=models.CASCADE
    )
    nazev = models.CharField(
        max_length=100
    )


class Catalog(models.Model):
    '''Catalog with selected products'''
    nazev = models.CharField(
        max_length=100
    )
    obrazek_id = models.ForeignKey(
        'Image',
        on_delete=models.PROTECT
    )
    products_ids = models.ManyToManyField(
        'Product'
    )
    attributes_ids = models.ManyToManyField(
        'Attribute'
    )