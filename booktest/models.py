from django.db import models

from tinymce.models import HTMLField


# Create your models here.
class GoodsInfo(models.Model):
    gcontent = HTMLField()


# 测试模型类
class GoodsTest(models.Model):
    STATUS_CHOICES = (
        # 选择项  元组
        (0, '下架'),
        (1, '上架')
    )
    # 代表商品状态  小整数
    status = models.SmallIntegerField(default=1, choices=STATUS_CHOICES, verbose_name='商品状态')
    detail = HTMLField(verbose_name='商品详情')  # 富文本编辑器

    class Meta:
        db_table = 'df_goods_test'
        verbose_name = '商品'
        verbose_name_plural = verbose_name  # 出去汉字后面的s
    '''
    mysql> desc df_goods_test;
    +--------+-------------+------+-----+---------+----------------+
    | Field  | Type        | Null | Key | Default | Extra          |
    +--------+-------------+------+-----+---------+----------------+
    | id     | int(11)     | NO   | PRI | NULL    | auto_increment |
    | status | smallint(6) | NO   |     | NULL    |                |
    | detail | longtext    | NO   |     | NULL    |                |
    +--------+-------------+------+-----+---------+----------------+
    3 rows in set (0.00 sec)
    '''

