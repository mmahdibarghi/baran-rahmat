from ast import Pass
from django.db.models import Sum
from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Payment)
class AdminPayment(admin.ModelAdmin):
    list_display=['pk',
                  'khayer',
                  'sandogh_khayerieh',
                  'tahvilgirandeh_sandogh',
                  'amount',
                  'date'
                  ]
    #list_editable=['date']
    ordering=['date']
    list_per_page=15

@admin.register(models.Khayer)
class AdminKhayer(admin.ModelAdmin):
    list_display=['pk',
                  'last_name',
                  'first_name',
                  'phone_number',
                  'sum_of_helps'
                  ]
    #list_editable=['first_name']
    #ordering=['']
    list_per_page=15

    def sum_of_helps(self,khayer):
        return khayer.sum_of_helps2
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            sum_of_helps2=Sum('payment__amount')
        )
    
@admin.register(models.HesabMoaseseh)
class AdminHesabMoaseseh(admin.ModelAdmin):
    list_display=['name',
                  'account_number',
                  'cart_number',
                  'sum_of_balance'
                  ]
    def sum_of_balance(self,hesab_moaseseh):
        return hesab_moaseseh.sum
    def get_queryset(self, request):# set fillter for save or pay

        return super().get_queryset(request).annotate(
            sum=Sum('payment__amount')
        )
        
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    
'''
@admin.register(models.Madadjo)
class AdminMadadjo(admin.ModelAdmin):
    list_display=['']
    list_editable=['']
    #ordering=['']
    list_per_page=15
    """
    @admin.display(ordering=)
    def sum_of_helps(self,khayer):
        Pass
    """
    

@admin.register(models.TahvilgirandehSandogh)
class AdminTahvilgirandehSandogh(admin.ModelAdmin):
    list_display=['']
    list_editable=['']
    #ordering=['']
    list_per_page=15

@admin.register(models.SandoghKhayerieh)
class AdminSandoghKhayerieh(admin.ModelAdmin):
    list_display=['']
    list_editable=['']
    #ordering=['']
    list_per_page=15

'''