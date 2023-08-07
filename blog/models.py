from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    head0 = models.CharField(max_length=500)
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500)
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500)
    chead2 = models.CharField(max_length=5000, default="")
    conclusion = models.CharField(max_length=5000, default="")
    pub_date  = models.DateField()
    publisher = models.CharField(max_length=100, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title[0:20] + " (" + str(self.post_id) + ")"