from asyncio import trsock
from datetime import date
from django.db import models

class Khayer(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    #national code can be null????/
    phone_number=models.CharField(max_length=12,null=True)
    address=models.TextField(null=True)
    post_code=models.CharField(max_length=10,null=True)
    #status    
    creating_date=models.TimeField(auto_now_add=True)
    #auto new add for first create
    
class SandoghKhayerieh(models.Model):
    
    #type
    #status
    #string_date
    khayer=models.ForeignKey(Khayer)
    #relation of sandog and khayer???????
class Assign(models.Model):
    date=models.TimeField(auto_now_add=True)
    
    sandogh_khayerieh=models.ForeignKey(SandoghKhayerieh,on_delete=models.PROTECT)
    tavilgirandeh=models.ForeignKey('TahvilgirandehSandogh',on_delete=models.PROTECT)
    
class TahvilgirandehSandogh(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    # national code can be null??????
    phone_number=models.CharField(max_length=12,null=False)
    #phone can be null?????
    create_date=models.TimeField(null=False,auto_now_add=True)
    
class Payment(models.Model):
    khayer=models.ForeignKey(Khayer,on_delete=models.PROTECT,null=True)
    sandogh=models.ForeignKey(SandoghKhayerieh,on_delete=models.PROTECT,null=True)
    tahvilgirandeh_sandogh=models.ForeignKey(TahvilgirandehSandogh,on_delete=models.PROTECT,null=True)
    hesab_moaseseh=models.ForeignKey('HesabMoaseseh',on_delete=models.PROTECT)
    #admin_id
    amount=models.BigIntegerField(null=False)
    date=models.DateField(auto_now=True)
    '''date for last modify or create date'''
    #type
    #authority
    #ref_code
    #has_paid
    card_number=models.CharField(max_length=16)
    """cart number or account number????"""
    #bank
    description=models.TextField(null=True)
class HesabMoaseseh(models.Model):
    name=models.CharField(max_length=255,null=False)
    account_number=models.CharField(max_length=10)
    """account number is nullable??"""
    cart_number=models.CharField(max_length=16)
    """cart number is nullable??"""

class Helping(models.Model):
    hesab_moaseseh=models.ForeignKey(HesabMoaseseh,on_delete=models.PROTECT)
    madadjo=models.ForeignKey('Madadjo',on_delete=models.PROTECT)
    amount=models.BigIntegerField()
    date=models.DateField(auto_now=True)
    '''date for last modify or create date'''

class Madadjo(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    phone_number=models.CharField(max_length=12,null=True)
    address=models.TextField(null=True)
    post_code=models.CharField(max_length=10,null=True)
    #status    
    creating_date=models.TimeField(auto_now_add=True)
    '''is all nullable??????????'''
    