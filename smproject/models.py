from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_list", kwargs={'pk' :self.pk})



class New(models.Model):
    news_user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_image = models.ImageField(null=True, blank=True, upload_to="images/")
    news_category = models.CharField(max_length=20)
    news_topic = models.CharField(max_length=100)
    news_details = models.CharField(max_length=2000)
    news_created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.news_topic

    def get_absolute_url(self):
        return reverse("new_list", kwargs={'id' :self.id})


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    commentator = models.CharField(max_length=100)
    commentator_position = models.CharField(max_length=50)

    def __str__(self):
        return self.commentator

    def get_absolute_url(self):
        return reverse("comment_list", kwargs={'id' :self.id})

class Client(models.Model):
    client_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def get_absolute_url(self):
        return reverse("client_list", kwargs={'pk' :self.pk})


class Portfolio(models.Model):
    news_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio_list", kwargs={'pk' :self.pk}) 

class Special(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    special_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("special_list", kwargs={'pk' :self.pk}) 


class Newsgrid(models.Model):
    ngrid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ngrid_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=20, default='uncategorized')
    ngrid_created_at = models.DateTimeField(default=datetime.now, blank=True)
    ngrid_description = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("special_list", kwargs={'pk' :self.pk}) 

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("special_list", kwargs={'pk' :self.pk}) 


class Parallax(models.Model):
    work_image = models.ImageField(null=True, blank=True, upload_to="images/")
    desc_work = models.CharField(max_length=1000)

    def __str__(self):
        return self.desc_work

    def get_absolute_url(self):
        return reverse("parallax_list", kwargs={'pk' :self.pk}) 


class Workgrid(models.Model):
    ngrid_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=20, default='uncategorized')
    ngrid_description = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("workgrid_list", kwargs={'pk' :self.pk})