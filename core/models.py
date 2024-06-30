from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return f"{self.category} / {self.name}"


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    date = models.DateField(default=now)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    duration = models.DurationField()
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return f"{self.activity} on {self.date}"
