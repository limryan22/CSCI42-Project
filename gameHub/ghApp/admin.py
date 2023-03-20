from django.contrib import admin
from .models import Account, userInfo

# Register your models here.

class accountAdmin(admin.ModelAdmin):
    model = Account
    list_display = (
        'username', 'password'
        )
    
class userInfoAdmin(admin.ModelAdmin):
    model = userInfo
    list_display = (
        'first_name', 'last_name', 'age'
    )

admin.site.register(Account, accountAdmin)
admin.site.register(userInfo, userInfoAdmin)
