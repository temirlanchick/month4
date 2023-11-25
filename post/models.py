from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} {self.title}"


class Category(models.Model):
    Product = models.ForeignKey(
        'post.Product',
        on_delete=models.CASCADE,
        related_name='category'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
