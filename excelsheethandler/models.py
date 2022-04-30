from django.contrib.auth import get_user_model
from django.db import models


class Employee(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='Employee',
        null=True,
    )
    empcode = models.CharField(max_length=10, default='')
    firstname = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.firstname

    # def save(self, *args, **kwargs):
    #     self.user = self.user
    #     super(Employee, self).save(*args, **kwargs)

    objects = models.Manager()


class EmployeeBulkUpload(models.Model):
    upload = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Employee/bulkupload/')
