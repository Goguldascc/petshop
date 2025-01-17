from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fn=models.CharField(max_length=50)
    mb=models.IntegerField()
    em=models.EmailField()
    ps=models.CharField(max_length=16)
    cps=models.CharField(max_length=16)

class pro_tbl(models.Model):
    pnm = models.CharField(max_length=25)
    pim =models.FileField(upload_to='pic')
    prc =models.IntegerField()
    des = models.TextField()

class cart_tbl(models.Model):
    customer = models.ForeignKey(reg_tbl,on_delete=models.CASCADE)
    product = models.ForeignKey(pro_tbl,on_delete=models.CASCADE) 
    qty =models.PositiveIntegerField(default=1)





