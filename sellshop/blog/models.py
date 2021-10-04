from django.db import models
from django.utils import timezone
from sellshop.utils.base_models import BaseModel


class Blog(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("account.User", on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Created_at")
    like = models.PositiveIntegerField(verbose_name="Like")
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, default="")

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(BaseModel):
    user_id = models.ForeignKey(
        "account.User", verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description")
    created_at = models.DateField(
        verbose_name="Created_at", default=timezone.now())
    blog_id = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True)
    comment_id = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default="", related_name="replies")

    def __str__(self) -> str:
        return f"{self.description}"
