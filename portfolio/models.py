from django.db import models

#inherents models class
class Project(models.Model):
    #all documentation available on Django website
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
