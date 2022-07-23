from django.db import models

class Khayer(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    phone_number=models.CharField(max_length=12,null=True)
    address=models.TextField(null=True)
    post_code=models.CharField(max_length=10,null=True)
    #status active nunactive moalagh
    creating_date=models.TimeField(auto_now_add=True)
    #auto new add for first create
    def __str__(self) -> str:
        return self.last_name +" "+ self.first_name
    class Meta:
        ordering=['last_name','first_name']
class SandoghKhayerieh(models.Model):
    PLASTICB='PLASTICB'
    PLASTICS='PLASTICS'
    FELEZIB='FELEZIB'
    FELEZIS='FELEZIS'
    type_choices=[
        (PLASTICB,'PlasticBig'),
        (PLASTICS,'PlasticBig'),
        (FELEZIB,'FeleziBig'),
        (FELEZIS,'FeleziSmall'),
        
    ]
    ACTIVE='ACTIVE'
    INACTIVE='INACTIVE'
    UNKNOWN='NUKKNOW'
    choices_status=[
        (ACTIVE,'Active'),
        (INACTIVE,'Inactive'),
        (UNKNOWN,'Unknown')            
                    ]
    code=models.CharField(max_length=255)
    typee=models.CharField(max_length=8,choices=type_choices)
    status=models.CharField(max_length=8,choices=choices_status,default=UNKNOWN)
    strting_date=models.DateField(auto_now_add=True)
    khayer=models.ForeignKey(Khayer,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.pk)
    class Meta:
        ordering=['pk']

class Assign(models.Model):
    date=models.TimeField(auto_now_add=True)
    sandogh_khayerieh=models.ForeignKey(SandoghKhayerieh,on_delete=models.PROTECT)
    tavilgirandeh=models.ForeignKey('TahvilgirandehSandogh',on_delete=models.PROTECT)
    
class TahvilgirandehSandogh(models.Model):
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    # national code can be null?????? yes
    phone_number=models.CharField(max_length=12,null=False)
    create_date=models.TimeField(null=False,auto_now_add=True)
    
    def __str__(self) -> str:
        return self.last_name +" "+ self.first_name
    class Meta:
        ordering=['last_name','first_name']

class Payment(models.Model):
    CART='CART'
    CASH='CASH'
    SANDOGH='SANDOGH'
    typechoice=[
        (CART,'Cart'),
        (CASH,'Cash'),
        (SANDOGH,'Sandogh'),
    ]
    khayer=models.ForeignKey(Khayer,on_delete=models.PROTECT,null=True,default=None,blank=True)
    sandogh_khayerieh=models.ForeignKey(SandoghKhayerieh,on_delete=models.PROTECT,null=True,default=None,blank=True)
    tahvilgirandeh_sandogh=models.ForeignKey(TahvilgirandehSandogh,on_delete=models.PROTECT,null=True,default=None,blank=True)
    hesab_moaseseh=models.ForeignKey('HesabMoaseseh',on_delete=models.PROTECT)
    #admin_id
    amount=models.BigIntegerField(null=False)
    date=models.DateField(auto_now=True)
    '''date for last modify or create date'''
    typee=models.CharField(max_length=7,choices=typechoice,default=CASH,null=True)
    #authority
    ref_code=models.CharField(max_length=12,null=True,blank=True)
    has_paid=models.CharField(max_length=12,null=True,blank=True)
    #max_length of ref and has ??????
    card_number=models.CharField(max_length=16)
    """cart number or account number????"""
    khayer_bank=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.pk)
    class Meta:
        ordering=['date']
        
        
class HesabMoaseseh(models.Model):
    name=models.CharField(max_length=255,null=False)
    account_number=models.CharField(max_length=10)
    
    cart_number=models.CharField(max_length=16)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=['name']

class Helping(models.Model):
    hesab_moaseseh=models.ForeignKey(HesabMoaseseh,on_delete=models.PROTECT)
    madadjo=models.ForeignKey('Madadjo',on_delete=models.PROTECT)
    amount=models.BigIntegerField()
    date=models.DateField(auto_now=True)
    '''date for create date'''

class Madadjo(models.Model):
    ACTIVE='ACTIVE'
    INACTIVE='INACTIVE'
    UNKNOWN='NUKKNOW'
    choices_status=[
        (ACTIVE,'Active'),
        (INACTIVE,'Inactive'),
        (UNKNOWN,'Unknown')            
                    ]
    first_name=models.CharField(max_length=255,null=False)
    last_name=models.CharField(max_length=255,null=False)
    national_code=models.CharField(max_length=10,null=True,unique=True)
    phone_number=models.CharField(max_length=12,null=True)
    address=models.TextField(null=True)
    post_code=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=8,choices=choices_status,default=UNKNOWN)
    creating_date=models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.last_name +" "+ self.first_name
    class Meta:
        ordering=['last_name','first_name']
    