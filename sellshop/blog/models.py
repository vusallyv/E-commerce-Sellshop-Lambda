from django.db import models
from django.utils import timezone
from sellshop.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _ 

class Blog(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Created_at", default=timezone.now())
    like = models.PositiveIntegerField(verbose_name="Like")
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, default="") 
    image = models.ImageField(verbose_name="Image", upload_to="blogs/")

    def __str__(self) -> str:
        return f"{self.title}"
                    

class Comment(BaseModel):
    user = models.ForeignKey(
        "user.User", verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description")
    created_at = models.DateField(
        verbose_name="Created_at", default=timezone.now())
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True)
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default="", related_name="replies")

    def __str__(self) -> str:
        return f"{self.description}"
