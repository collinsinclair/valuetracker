import datetime

from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Valued Activity"
        verbose_name_plural = "Valued Activities"


class Entry(models.Model):
    date = models.DateField(default=datetime.date.today, unique=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%-d %b %Y")

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"


class ActivityEntry(models.Model):
    entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, related_name="activity_entries"
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="activity_entries"
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.activity.name} on {self.entry.date.strftime('%-d %b %Y')}"

    class Meta:
        verbose_name = "Activity Entry"
        verbose_name_plural = "Activity Entries"
