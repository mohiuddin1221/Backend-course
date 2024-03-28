from django.db import models

# Create your models here.

class TimestampModel(models.Model):
    """
    Abstract base class model that provides self-managed "created at" and "updated at" fields.
    """

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Category(TimestampModel):
    category_name = models.CharField(max_length =150)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    
    def __str__(self) :
        return self.category_name

class Product(TimestampModel):
    product_name = models.CharField(max_length = 150)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    product_Description = models.TextField()
    price = models.DecimalField(max_digits =10, decimal_places =2)
    image = models.ImageField(upload_to='products/images/')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.product_name

class Order(TimestampModel):
    customer_name = models.CharField(max_length = 150)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.customer_name
    
