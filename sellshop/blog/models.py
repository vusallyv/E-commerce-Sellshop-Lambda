from django.db import models
from sellshop.utils.base_models import BaseModel



class Blog(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.CharField("Creator", max_length=30, help_text="Max 30 char.")
    like = models.IntegerField(verbose_name="Like")
    brand_id = models.ForeignKey('product.Brand', on_delete=models.CASCADE)
    category_id = models.ForeignKey('product.Category', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class Comment(BaseModel):
    description = models.TextField(verbose_name="Description")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('blog.Comment', on_delete=models.CASCADE)
    