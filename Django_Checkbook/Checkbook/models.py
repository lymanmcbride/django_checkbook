from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    accounts = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

transaction_types = [('Deposit', 'Deposit'), ('Withdrawl', 'Withdrawl')]

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices = transaction_types)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()


