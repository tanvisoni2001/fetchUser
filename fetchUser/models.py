from django.db import models

# Create your models here.

class fetchUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 26)
    email = models.EmailField(max_length = 26)
    full_name = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 12)

    def __str__(self):
        return self.username


