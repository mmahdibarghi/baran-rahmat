from ast import Pass
from django.db.models import Sum
from django.contrib import admin
from django.http import HttpResponse
from . import models
# Register your models here.
import pandas as pd

def export_to_excel(modeladmin, request, queryset):
    # create a list to hold the data for the DataFrame
    data = []

    # iterate over the selected Payment objects
    for payment in queryset:
        # fetch the related data
        khayer = payment.khayer.first_name + ' ' + payment.khayer.last_name if payment.khayer else None
        sandogh_khayerieh = payment.sandogh_khayerieh.code if payment.sandogh_khayerieh else None
        tahvilgirandeh_sandogh = payment.tahvilgirandeh_sandogh.first_name + ' ' + payment.tahvilgirandeh_sandogh.last_name if payment.tahvilgirandeh_sandogh else None
        hesab_moaseseh = payment.hesab_moaseseh.name

        # extract the year, month, and day from the date field
        year = payment.date.year
        month = payment.date.month
        day = payment.date.day

        # add a row of data for this Payment object
        data.append({
            'id': payment.id,
            'khayer': khayer,
            'sandogh_khayerieh': sandogh_khayerieh,
            'tahvilgirandeh_sandogh': tahvilgirandeh_sandogh,
            'hesab_moaseseh': hesab_moaseseh,
            'amount': payment.amount,
            'year': year,
            'month': month,
            'day': day,
            'typee': payment.typee,
            'authority': payment.authority,
            'ref_code': payment.ref_code,
            'has_paid': payment.has_paid,
            'card_number': payment.card_number,
            'khayer_bank': payment.khayer_bank,
            'description': payment.description,
        })

    # create a DataFrame from the data
    df = pd.DataFrame(data)

    # create an Excel file from the DataFrame
    with pd.ExcelWriter('payments.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Payments')

    # serve the Excel file as a downloadable response
    with open('payments.xlsx', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=payments.xlsx'
        return response

export_to_excel.short_description = "Export selected payments to Excel"

@admin.register(models.Payment)
class AdminPayment(admin.ModelAdmin):
    list_display=['pk',
                  'khayer',
                  'sandogh_khayerieh',
                  'tahvilgirandeh_sandogh',
                  'amount',
                  'date'
                  ]
    search_fields=['pk',
                  'khayer__first_name',
                  'khayer__last_name',
                  'sandogh_khayerieh__code',
                  'tahvilgirandeh_sandogh__first_name',
                  'tahvilgirandeh_sandogh__last_name',
                  'amount',
                  ]
    #list_editable=['date']
    autocomplete_fields = ['khayer','sandogh_khayerieh','tahvilgirandeh_sandogh']
    list_filter=[
        'id',
        'date',
        'khayer',
        'sandogh_khayerieh',
        'tahvilgirandeh_sandogh',
                ]
    ordering=['date']
    list_per_page=15
    actions = [export_to_excel]
@admin.register(models.Khayer)
class AdminKhayer(admin.ModelAdmin):
    list_display=['pk',
                  'last_name',
                  'first_name',
                  'phone_number',
                  'sum_of_helps',
                  'creating_date'
                  ]
    search_fields=[
        'pk',
                  'last_name',
                  'first_name',
                  'phone_number',
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
    search_fields=['name']
    def sum_of_balance(self,hesab_moaseseh):
        if hesab_moaseseh.Pay != None and hesab_moaseseh.Recive !=None:
            return hesab_moaseseh.Recive - hesab_moaseseh.Pay
        elif hesab_moaseseh.Pay == None:
            return hesab_moaseseh.Recive
        else:
            return (-1)*hesab_moaseseh.Pay
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            
            Recive=Sum('payment__amount'),
            Pay=Sum('helping__amount')
            
        )
        
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    


@admin.register(models.Madadjo)
class AdminMadadjo(admin.ModelAdmin):
    list_display=['first_name',
                  'last_name',
                  'status',
                  'sum_of_helped_recived',
                  'creating_date'
                  ]
    
    search_fields=[
                'pk',
                'last_name',
                'first_name',
                'phone_number',
                'status',
    ]

    
    list_per_page=15
    def sum_of_helped_recived(self,madadjo):
        return madadjo.sum
    def get_queryset(self, request):# set fillter for save or pay

        return super().get_queryset(request).annotate(
            sum=Sum('helping__amount')
        )
        
    #list_editable=['']
    #ordering=['']
    list_per_page=15
       

@admin.register(models.TahvilgirandehSandogh)
class AdminTahvilgirandehSandogh(admin.ModelAdmin):
    list_display=['first_name',
                  'last_name',
                  'phone_number'
                  ]
    search_fields=['first_name',
                  'last_name',
                  'phone_number'
                  ]
    #list_editable=['']
    #ordering=['']
    list_per_page=15

@admin.register(models.SandoghKhayerieh)
class AdminSandoghKhayerieh(admin.ModelAdmin):
    list_display=['pk',
                  'khayer'
                  ]
    search_fields=[
        'pk',
        'khayer__first_name',
        'khayer__last_name',
        ]
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    autocomplete_fields = ['khayer','khayer_ghabli']
@admin.register(models.Helping)
class AdminHelping(admin.ModelAdmin):
    list_display=['madadjo',
                  'hesab_moaseseh',
                  'amount',
                  'date'
                  ]
    
    search_fields=['madadjo__first_name',
                   'madadjo__last_name',
                  'hesab_moaseseh__name',
                  'amount',
                  'date'
                  ]
    #list_editable=['']
    autocomplete_fields = ['madadjo']
    ordering=['date']
    list_per_page=15

