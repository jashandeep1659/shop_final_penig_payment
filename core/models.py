from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',)
    name = models.CharField(max_length=200, db_index=True)
    brand_name = models.CharField(max_length=100, default='Deep Store')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d',blank=True, null=True)
    description = HTMLField()
    price  = models.DecimalField(max_digits=8, decimal_places=2, )
    available = models.BooleanField(default=True)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, editable=True)


    class Meta:
        ordering = ['-updated']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name



class Top_banner(models.Model):
    title = models.CharField(max_length=50)
    offer = models.CharField(max_length=100,)
    para =  HTMLField()
    link_page = models.CharField(max_length=300,)
    images_of_item = models.ImageField(upload_to='banner/images',blank=True,null=True)
    image_background = models.ImageField(upload_to='banner/bg_images',blank=True,null=True)

    def __str__(self):
        return self.title       




class Deal(models.Model):
    product_id = models.IntegerField()
    off_percentage = models.CharField(max_length=100, null=True,blank=True)
    updated=  models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        ordering = ['-updated']

    def __int__(self):
        return self.product_id


