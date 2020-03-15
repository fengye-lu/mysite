from django.db import models


'''
创建好数据库表后，在命令行窗口输入下面两条命令生成表，或更新表
python manage.py makemigrations
python manage.py migrate
'''


# Create your models here.
# ORM相关的只能写在这个文件里，写到别的文件里Django找不到

class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    year = models.IntegerField()


    def __str__(self):
        return self.username


# class Test(models.Model):
#     name = models.CharField(max_length=64)
#     hometown = models.TextField() # TestField跟CharField比存的更长的内容

#
# class Study(models.Model):
#     id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
#     name = models.CharField(null=False, max_length=20)  # 创建一个varchar类型的不能为空的字段


# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=32)
#
#     publisher = models.ForeignKey(
#         to='Publisher',
#         on_delete=models.CASCADE,  # 删除关联数据时，应该怎么处理，这里是默认的级联操作
#         related_name='books',  # 反向查询的时候用来代替表名_set
#         related_query_name='xxoo',  # 反向双下划线跨表查询是用来代替表名
#     )

    # author = models.ManyToManyField('Author')  实现多对多
