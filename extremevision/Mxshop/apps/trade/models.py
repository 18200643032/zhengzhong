from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
User = get_user_model()
# Create your models here.



class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User,verbose_name=u"用户",on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,verbose_name=u"商品",on_delete=models.CASCADE)
    nums = models.IntegerField(default=0,verbose_name="购买数量")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ("user","goods")

    def __str__(self):
        return f"{self.goods.name}({self.nums})"


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS","成功"),
        ("TRADE_CLOSED","超时关闭"),
        ("WAIT_BUYER_PAY","交易创建"),
        ("TRADE_FINISHED","交易结束"),
        ("paying","待支付")
    )