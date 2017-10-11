from django.db import models

class Update_Form(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
