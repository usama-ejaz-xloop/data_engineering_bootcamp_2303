from django.db import models


class TODOItem(models.Model):
    content = models.TextField()
