from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

@admin.register(FeeReport)
class FeeReport(admin.ModelAdmin):
    list_display = ('id','gid','totalFee','DueTutionFee','DueDevelopmentFee','DueOtherFee','TotalDueFee','FeeDetail')

@admin.register(FeeTransaction)
class FeeTransaction(admin.ModelAdmin):
    list_display = ('id','gid','txnId','txnAmt','txnReciept')
