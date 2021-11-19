from django.db import models
from django.utils import timezone
from sellshop.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Blog(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("user.User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, default="")
    image = models.ImageField(verbose_name="Image", upload_to="blogs/")

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(BaseModel):
    user = models.ForeignKey(
        "user.User", verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="blogs_comment")
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default="", related_name="replies", verbose_name="Reply to")
    is_main = models.BooleanField(verbose_name="Is Main?", default=False)

    def __str__(self) -> str:
        return f"{self.description}"
