from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    nomi = models.CharField(max_length=155)
    mazmuni = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nomi}"
    
class News(models.Model):
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        
    nomi = models.CharField(max_length=255, null=False)
    mazmuni = models.TextField(null=False)
    koriwlar_soni = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="news-image", null=True, blank=True)
    holati = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}, --- {self.nomi}"