from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Product Class

#title
#url
#pub_date
#votes_total
#image
#icon
#body

#pub_date_pretty

#hunter


class Product(models.Model):

    title = models.CharField(max_length=255)
    url = models.TextField(default='')
    pub_date = models.DateTimeField(default=datetime.now)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField(default='')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')



