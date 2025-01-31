from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True, related_name="tags")

    def status(self):
        return "Done" if self.is_done else "Not done"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
