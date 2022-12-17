from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser


class NotSignedHome(models.Model):
    main_title = models.CharField(max_length=255, default="")
    main_paragraph= models.TextField()

    overview_title = models.CharField(max_length=255, default="")

    overview_img_desc = models.CharField(max_length=255, default="")
    overview_img = models.ImageField(upload_to='upload/')

    calories_img_desc = models.CharField(max_length=255, default="")
    calories_img = models.ImageField(upload_to='upload/')

    body_measurements_img_desc = models.CharField(max_length=255, default="")
    body_measurements_img = models.ImageField(upload_to='upload/')

    about_title = models.CharField(max_length=255, default="")
    about_paragraph= models.TextField(default="")

    sevices_title = models.CharField(max_length=255, default="")
    sevices_paragraph= models.TextField(default="")

    s1_title = models.CharField(max_length=255, default="")
    s1_paragraph= models.TextField(default="")

    s2_title = models.CharField(max_length=255, default="")
    s2_paragraph= models.TextField(default="")

    s3_title = models.CharField(max_length=255, default="")
    s3_paragraph= models.TextField(default="")

    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.main_title
