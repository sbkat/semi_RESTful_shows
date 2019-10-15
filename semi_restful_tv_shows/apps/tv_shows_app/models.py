from django.db import models
from datetime import datetime

class ShowUser(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        title_from_form = Show.objects.filter(title=postData['title'])
        if postData['title'] == title_from_form[0].title:
            errors['title'] = "Title is already in database. Try again."
        if len(postData['title']) < 2:
            errors['title'] = "Title should be more than 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network should be more than 3 characters."
        if len(postData['description']) != 0:
            if len(postData['description']) < 10:
                errors['description'] = "Description should be more than 10 characters."
        if postData['release_date'] > str(datetime.now()):
            errors['release_date'] = "Cannot process a future release date."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowUser()
