from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class About(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to="index/img")
    offer = models.CharField(max_length=50)
    offer2 = models.CharField(max_length=50)
    offer3 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Our(models.Model):
    name = models.CharField(max_length=505)
    text = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Popular(models.Model):
    shax=models.CharField(max_length=5)
    img=models.ImageField(upload_to="index/img")
    cheg=models.TextField(max_length=5)
    def __str__(self):
        return self.shax

class Avesome(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="index/img")
    data=models.IntegerField()
    nomber=models.IntegerField()
    kal=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Easy(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Meet(models.Model):
    name=models.CharField(max_length=10)
    img=models.ImageField(upload_to="index/img")
    titl=models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Aur(models.Model):
    name=models.CharField(max_length=50)
    contry=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    img=models.ImageField(upload_to="index/img")
    def __str__(self):
        return self.name




class Comment(models.Model):
    about=models.ForeignKey(About, on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=False, blank=False)
    created_at=models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tips.name}"





class Forma (models.Model):
    DESTINATION_CHOISE={
        'usa':'USA',
        'italy':'Italiy',
        'china':'China',
        'japan':'Japan',
        'mexicO':'Mexico',
    }
    name=models.CharField(max_length=50)
    email=models.EmailField()
    destination=models.CharField(max_length=500, choices=DESTINATION_CHOISE,default='usa')
    request=models.TextField(blank=True, null=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.name
