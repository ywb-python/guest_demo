from django.db import models


# 发布会记录表
class Event(models.Model):
    name = models.CharField("发布会的标题", max_length=100)
    limit = models.IntegerField("参加人数")
    status = models.BooleanField("状态")
    address = models.CharField("地址", max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField("创建时间(自动获取当前时间)", auto_now=True)

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)
    real_name = models.CharField("姓名", max_length=64)
    phone = models.CharField("手机号", max_length=16)
    email = models.EmailField("邮箱")
    sign = models.BooleanField("签到状态")
    create_time = models.DateTimeField("创建时间(自动获取当前时间)", auto_now=True)

    class Meta:
        # 设置联合主键
        unique_together = ("event", "phone")

    def __str__(self):
        return self.real_name
# Create your models here.
