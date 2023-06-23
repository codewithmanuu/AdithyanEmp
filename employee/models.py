from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.CharField(max_length=20,null=True)
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    designation = models.CharField(max_length=20)
    team=models.CharField(max_length=20,null=True)
    salary=models.TextField(null=True)
    phonenumber=models.CharField(max_length=12,null=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            last_object = self.__class__.objects.last()
            if last_object:
                last_id = int(last_object.employee_id.split('-')[1])
                new_id = f"EMP-{str(last_id + 1).zfill(3)}"
            else:
                new_id = "EMP-001"
            self.employee_id = new_id

        super().save(*args, **kwargs)

    def __str__(self):
        return self.firstname



class Employee_leaves(models.Model):
    leaves = (
        ('Half day', 'Half day'),
        ('Full day', 'Full day')

    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    leave_type = models.CharField(max_length=300, choices=leaves)
    purpose=models.TextField()

def __str__(self):
    return str(self.employee)
