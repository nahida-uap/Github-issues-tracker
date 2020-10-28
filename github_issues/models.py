from django.db import models

class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    issue_id = models.CharField(max_length=10, blank=False, unique=True)
    title = models.CharField(max_length=2000, blank=True)
    state = models.CharField(max_length=60, blank=True)
    url = models.CharField(max_length=256, blank=False, unique=True)
    detail = models.CharField(max_length=10000, blank=False)
