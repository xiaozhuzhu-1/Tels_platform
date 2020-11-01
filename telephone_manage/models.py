from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# django ORM
class tels(models.Model):
    # 创建项目表，以下为表述字段
    name = models.CharField("所属人",max_length=100,null=False,default="")
    fund = models.CharField("所属资产",choices=(('个人','个人'),('公司','公司')), max_length=100, null=False, default="")
    sys = models.CharField("系统", choices=(('IOS','IOS'),('Android','Android')),max_length=100, null=False, default="")
    # sys = (1,'IOS'),(2,'Android')
    type = models.CharField("型号", max_length=100, null=False, default="")
    version = models.CharField("版本", max_length=100, null=False, default="")

    # 精确到 年-月-日
    creat_time = models.DateField("创建时间",auto_now_add=True)

    # 精确到年-月-日 时：分：秒  在前端使用事直接匹配即可 Y-m-d H:i:s
    update_time = models.DateTimeField("更新时间", auto_now=True)


    class Meta:
        ordering = ['-creat_time', '-id']