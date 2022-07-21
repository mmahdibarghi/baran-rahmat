from ast import Pass
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
    #ordering=['date']
    list_per_page=15

#@admin.register(models.Khayer)
#class AdminKhayer(admin.ModelAdmin):
#    list_display=['pk','first_name']
#    list_editable=['first_name']
#    #ordering=['']
#    list_per_page=15

    '''
    @admin.display(ordering=)
    def sum_of_helps(self,khayer):
        Pass
    '''
    

@admin.register(models.HesabMoaseseh)
class AdminHesabMoaseseh(admin.ModelAdmin):
    list_display=['name']
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    """
    @admin.display(ordering=)
    def sum_of_helps(self,khayer):
        Pass
    """
    #sum_of_balance
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