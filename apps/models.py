from django.db.models import Model, CASCADE, ImageField, CharField, SlugField, FloatField, TextField, DateTimeField, \
    ForeignKey
from django.utils.text import slugify


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(SlugBaseModel):
    pass


class Product(CreatedBaseModel, SlugBaseModel):
    price = FloatField(default=0)
    description = TextField(null=True, blank=True)
    image = ImageField(null=True, blank=True, upload_to='products')
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
