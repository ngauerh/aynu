from django.db import models

# Create your models here.


class Work(models.Model):
    job_url = models.CharField(max_length=125)  # 职位详情链接
    job_comp = models.CharField(max_length=50)  # 公司名
    job_name = models.CharField(max_length=20)  # 职位名
    job_smoney = models.IntegerField(max_length=10)  # 最少薪资
    job_emoney = models.IntegerField(max_length=10)  # 最大薪资
    job_address = models.CharField(max_length=20)  # 工作地点
    job_comp_type = models.CharField(max_length=10)  # 公司类别
    job_comp_snum = models.IntegerField(max_length=10)  # 公司规模 最少人数
    job_comp_enum = models.IntegerField(max_length=10)  # 最大人数
    job_business = models.CharField(max_length=125)  # 公司主营
    job_syear = models.IntegerField(max_length=10)  # 经验要求 最小
    job_eyear = models.IntegerField(max_length=10)  # 最大经验年限
    job_date_pub = models.CharField(max_length=10)  # 发布日期
    job_datetime = models.CharField(max_length=10)  # 收录时间
    job_welfafe = models.CharField(max_length=125)  # 公司福利
    job_people = models.CharField(max_length=125)  # 招聘人数
    job_desc = models.CharField(max_length=125)  # 岗位职责
    job_request = models.CharField(max_length=125)  # 岗位要求
    job_tag = models.CharField(max_length=10)  # 工作标签
    job_degree = models.CharField(max_length=10)  # 学历

    class Meta:
        db_table = "job"  # 更改表名