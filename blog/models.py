from django.db import models


'''
创建好数据库表后，在命令行窗口输入下面两条命令生成表，或更新表
python manage.py makemigrations
python manage.py migrate
'''


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    year = models.IntegerField()


    def __str__(self):
        return self.username


class Test(models.Model):
    name = models.CharField(max_length=64)
    hometown = models.TextField() # TestField跟CharField比存的更长的内容