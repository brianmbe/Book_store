import code
from tabnanny import verbose
from turtle import title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.name}, ({self.code})'


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Point"

    """
    def get_absolute_url(self):
        return reverse("Adress_detail", kwargs={"pk": self.pk})
    """


class Author(models.Model):
    # Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    """
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    """


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} (Ratings: {self.ratings} and Bestseller: {self.is_bestselling})"

    # Overwriting the inbuilt save() in mysql
    # Giving the user the right to input his/her slug
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    """
