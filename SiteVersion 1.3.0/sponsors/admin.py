from django.contrib import admin
from .models import (SponsorModel,
                    SponsorClassModel,
                    MemberModel,
                    StaffModel,
                    Header,
                    CommunityBlock,
                    HistoryBlock,                  
                    ContactModel)

# Register your models here.


'''
class SponsorClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortcode']
    prepopulated_fields = {'shortcode': ('name',)}
    
admin.site.register(SponsorClassModel, SponsorClassAdmin)
'''


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(SponsorModel, SponsorAdmin)
    
admin.site.register(MemberModel)

admin.site.register(StaffModel)

admin.site.register(Header)

admin.site.register(CommunityBlock)

admin.site.register(HistoryBlock)

admin.site.register(ContactModel)
