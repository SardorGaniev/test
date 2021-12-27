from django.db import models



class Product(models.Model):
    FILTER = (
        ('DRINKS', 'DRINKS'),
        ('FAST-FOOD', 'FAST-FOOD'),
        ('UZBEK', 'UZBEK'),
        ('SALADS', 'SALADS'),
    )
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    filter = models.CharField(max_length=200, null=True, choices=FILTER)

    def __str__(self):
        return self.name


class Stuff(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.TextField(blank=True)
    image = models.ImageField(upload_to='stuff/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.fullname


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    your_text = models.CharField(max_length=200)
    select = models.CharField(max_length=100)

    def __str__(self):
        return self.name
