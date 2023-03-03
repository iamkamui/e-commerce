from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(_("Name"), max_length=50)
    category_description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    deleted_at = models.DateTimeField(_("Deleted at"), auto_now_add=True)

    

    def __str__(self):
        return self.category_name
    
class Gender(models.Model):
    gender_name = models.CharField(_("Name"), max_length=50)
    gender_description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    deleted_at = models.DateTimeField(_("Deleted at"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Gender")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.gender_name

    

class Product(models.Model):
    product_name = models.CharField(_("Name"), max_length=100)
    product_price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    prodruct_description = models.TextField(_("Description"))
    SKU = models.CharField(_("SKU"), max_length=50)
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    gender_id = models.ForeignKey(Gender, verbose_name=_("Gender"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    deleted_at = models.DateTimeField(_("Deleted at"), auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})