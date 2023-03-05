from django.db import models
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
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
        return f'{self.category_name}'
    
class Gender(models.Model):
    gender_name = models.CharField(_("Name"), max_length=50)
    gender_description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    deleted_at = models.DateTimeField(_("Deleted at"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Gender")
        verbose_name_plural = _("Genders")

    def __str__(self):
        return self.gender_name

    

class Product(models.Model):
    product_name = models.CharField(_("Name"), max_length=100)
    mainproduct_image = models.ImageField(_("Main Product Image"), upload_to="main_image", max_length=None, blank=True)
    product_price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    prodruct_description = models.TextField(_("Description"))
    SKU = models.CharField(_("SKU"), max_length=50)
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    gender_id = models.ForeignKey(Gender, verbose_name=_("Gender"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    deleted_at = models.DateTimeField(_("Deleted at"), auto_now_add=True)

    def custom_slugify(value):
        return default_slugify(value).replace(' ', '-')
    
    slug = AutoSlugField(populate_from='product_name',
                         unique_with=['id__id', 'created_at__month'],
                         slugify=custom_slugify)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})