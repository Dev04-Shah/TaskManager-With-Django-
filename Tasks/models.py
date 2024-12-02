from django.db import models

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=500)
    client_image = models.ImageField(upload_to='Tasks/Clients')
    task_image = models.ImageField(upload_to='Tasks/OurImages')
    video = models.URLField(max_length=500, blank=True, null=True)  # New field
    remarks = models.TextField(blank=True, null=True)  # New field
