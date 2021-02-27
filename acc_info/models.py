from django.db import models

class AccountHead(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    acc_type_name = models.CharField(max_length = 100)
    acc_head = models.ForeignKey(AccountHead, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_type_name

class AccountName(models.Model):
    acc_name = models.CharField(max_length = 100)
    type_of_acc = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    opening_balance = models.FloatField()
    closing_balance = models.FloatField()

    def __str__(self):
        return self.acc_name

class JournalLog(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_no = models.CharField(max_length = 100)

    def __str__(self):
        return self.reference_no

class JournalLogDetail(models.Model):
    journal_log = models.ForeignKey(JournalLog, on_delete=models.CASCADE)
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return self.amount

