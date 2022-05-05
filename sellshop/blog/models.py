from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from sellshop.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class Blog(BaseModel):
    title = models.CharField("Title", max_length=30, help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    creator = models.ForeignKey("user.User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "product.ProductVersion", on_delete=models.CASCADE, default="")
    image = models.ImageField(verbose_name="Image", upload_to="blogs/")
    slug = models.SlugField(max_length=30, unique=True)
    typing_users = models.ManyToManyField("user.User", related_name="typing_users")
    online_users = models.ManyToManyField("user.User", related_name="online_users")

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)


class Comment(BaseModel):
    user = models.ForeignKey(
        "user.User", verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="blogs_comment")
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default="", verbose_name="Parent Comment")
    is_main = models.BooleanField(verbose_name="Is Main?", default=False)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"""
            {self.user.username} commented {self.description} on {self.blog.title}
        """
