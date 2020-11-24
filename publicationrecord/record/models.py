from django.db import models

# Create your models here.


class RecordListItem(models.Model):
    title = models.CharField(max_length=200, null=True)
    UniqueID = models.CharField(max_length=200, null=True)
    authorname = models.CharField(max_length=200, null=True)
    publicationname = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.UniqueID
