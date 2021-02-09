from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    titleimg = models.ImageField(blank=True, null=True)
    introduction = models.TextField()
    subtitle1 = models.CharField(max_length=50)
    subimg1 = models.ImageField(blank=True, null=True)
    subcontents1 = models.TextField()
    subtitle2 = models.CharField(max_length=50)
    subimg2 = models.ImageField(blank=True, null=True)
    subcontents2 = models.TextField()
    subtitle3 = models.CharField(max_length=50)
    subimg3 = models.ImageField(blank=True, null=True)
    subcontents3 = models.TextField()
    conclusiontitle = models.CharField(max_length=50)
    conclusionimg = models.ImageField(blank=True, null=True)
    conclusioncontents = models.TextField()

    def __str__(self):
        return self.title