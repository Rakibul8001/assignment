from django.contrib import admin
from .models import AccountHead,AccountType,AccountName,JournalLog,JournalLogDetail
# Register your models here.

admin.site.register(AccountHead)
admin.site.register(AccountType)
admin.site.register(AccountName)
admin.site.register(JournalLog)
admin.site.register(JournalLogDetail)