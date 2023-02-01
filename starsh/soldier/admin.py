from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _
from .models import (MilitaryRank, Platoon, ServiseID, Unit, OfficialPosition, Company,
                     Education, Creed, Nationality, Command, Region, State)
#from osoba.widgets import CustomDatePickerInput


class ServiseIDAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {
        #    'fields': ('field1', 'field2', 'field3')
        # }),
        (_('Main data'), {
            'fields': ('name', 'sename', 'third_name', 'birth_date', 'nickname')
        }),
        (_('Names in accs'), {  # давальний відмінок
            'fields': ('name_accs', 'sename_accs', 'third_name_accs')
        }),
        (_('Company'), {
            'fields': ('military_ranks',)
        }),

        (_('Info for Service begin'), {
            'fields': ('military_office', 'date_of_conscription', 'order_date', 'order_number')
        }),

        (_('General information'), {
            'fields': ('orphan',
                       'married', 'halforphan', 'work', 'mobilization', 'driveid', 'driveid_category', 'creed',
                       'nationality', 'education', 'blood_type', 'rh')
        }),

        (_('militaryID'), {
            'fields': ('militaryID_seria', 'militaryID_number', 'who_militaryID',
                       'militaryID_date', 'weapon', 'military_rank_id', 'military_rank_date')
        }),

        (_('ID'), {
            'fields': ('ID_seria', 'ID_number', 'who_ID',
                       'ID_date', 'ipn')
        }),

        (_('Address'), {
            'fields': ('state_pr', 'region_pr', 'postal_code_pr', 'addres_pr',
                       'state_fact', 'region_fact', 'addres_fact', 'postal_code_fact',
                       'phone1', 'phone2', 'father', 'mother', 'partner')

        }),
        (_('Images'), {
            'fields': ('image_face3x4',)

        })
    )
    # change_form_template = 'admin/ocoba_change_form.html'
    # formfield_overrides = {
    #         models.DateField: {'widget': MonthPickerInput}
    #     }


admin.site.register(Company)
admin.site.register(MilitaryRank)
admin.site.register(Platoon)
admin.site.register(ServiseID, ServiseIDAdmin)
admin.site.register(Unit)
admin.site.register(OfficialPosition)
admin.site.register(Creed)
admin.site.register(Nationality)
admin.site.register(Education)
admin.site.register(Command)
admin.site.register(State)
admin.site.register(Region)
