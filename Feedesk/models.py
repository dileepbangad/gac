from django.db import models

# Create your models here.
class FeeReport(models.Model):
    gid = models.CharField(max_length=9,unique=True,null=False)
    totalFee = models.BigIntegerField()
    DueTutionFee = models.BigIntegerField()
    DueDevelopmentFee = models.BigIntegerField()
    DueOtherFee = models.BigIntegerField()
    TotalDueFee = models.BigIntegerField()
    FeeDetail = models.FileField(upload_to='feeDetail/')
    class Meta:
        verbose_name = ("Fee Desk")
    def __str__(self)->str:
        return self.gid

class FeeTransaction(models.Model):
    gid = models.CharField(max_length=9,unique=True,null=False)
    txnId = models.CharField(max_length=50)
    txnAmt = models.BigIntegerField()
    txnReciept = models.FileField(upload_to='txnReciept/')
    class Meta:
        verbose_name = ("Fee Transactions")
    def __str__(self)->str:
        return self.gid