from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=11)
    desc = models.TextField()
    date = models.DateField()
    # craeted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # This will return the name of the contact in the admin panel