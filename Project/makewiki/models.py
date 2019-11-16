from django.db import models

# Create your models here.


class Database(models.Model):

    title = models.CharField(max_length=100)
    # date goes here 
    authur = models.CharField(max_length=300)
    summery =  models.CharField(max_length=300)
    body =  models.TextField()



    def __stry__(self):
        return self.title
