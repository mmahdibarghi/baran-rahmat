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
    
class SandoghKhayrieh(models.Model):
    #khayer_id
    #type
    #status
    #string_date
    pass
class Assign(models.Model):
    #tavilgirandeh_id
    #sandogh_id
    date=models.TimeField(auto_now_add=True)
    
class TahvilgirandehSandogh(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    # national code can be null??????
    phone_number=models.CharField(max_length=12,null=False)
    #phone can be null?????
    create_date=models.TimeField(null=False,auto_now_add=True)
    
class Payment(models.Model):
    #khayer_id
    #sandogh_id
    #tahvilgirandeh_id
    #accunt_id
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
    #account_id
    #madadjo_id
    amount=models.BigIntegerField()
    date=models.DateField(auto_now=True)
    '''date for last modify or create date'''

class madadjo(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    phone_number=models.CharField(max_length=12,null=True)
    address=models.TextField(null=True)
    post_code=models.CharField(max_length=10,null=True)
    #status    
    creating_date=models.TimeField(auto_now_add=True)
    '''is all nullable??????????'''
    