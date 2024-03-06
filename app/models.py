from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
