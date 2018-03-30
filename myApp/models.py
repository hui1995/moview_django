from datetime import datetime

from django.db import models

# Create your models here.


class Banner(models.Model):

    bannerid =models.IntegerField()
    type=models.IntegerField()
    object_id=models.IntegerField()
    title=models.CharField(max_length=30)
    url=models.CharField(max_length=100)
    image=models.CharField(max_length=150)
    description=models.CharField(max_length=320)
    userid=models.IntegerField()
    addtime=models.CharField(max_length=30)
    uptime=models.CharField(max_length=30)
    orderid=models.IntegerField()
    cateid=models.IntegerField()
    count_click=models.IntegerField()




class Moview(models.Model):
    postid =models.IntegerField()
    title=models.CharField(max_length=120)
    de=models.CharField(max_length=150)
    pid=models.IntegerField()
    publish_time=models.IntegerField()
    like_num=models.IntegerField()
    share_num=models.IntegerField()
    post_type=models.IntegerField()
    image=models.CharField(max_length=100)
    request_url=models.CharField(max_length=100)
    ispromote=models.IntegerField()
    isalbum=models.IntegerField()




class User(models.Model):

    usernmae=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    image=models.ImageField(upload_to='media')
    # touken验证值，每次登陆之后都会更新
    userToken = models.CharField(max_length=50)

    @classmethod
    def createuser(cls, account, passwd, email, img, token):
        u = cls(usernmae=account, password=passwd, email=email, image=img, userToken=token)
        return u

class Like(models.Model):

    uid =models.ForeignKey(User)
    mid=models.ForeignKey(Moview)






