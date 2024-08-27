from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='device_pics/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

class Order(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.student_name} - {self.device.name}"

