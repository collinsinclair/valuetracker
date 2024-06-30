from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories",
        editable=False,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activities",
        editable=False,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="activities")

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        category_names = ", ".join(category.name for category in self.categories.all())
        return f"{category_names} / {self.name}"


class Entry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="entries",
        editable=False,
    )
    date = models.DateField(default=now)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    duration = models.DurationField()
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return f"{self.activity} on {self.date}"
