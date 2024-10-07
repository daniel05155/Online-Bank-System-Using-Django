from django.db import models
from django.contrib.auth.models import AbstractUser

# Gender 選項
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

# Account Type 選項
ACCOUNT_TYPE_CHOICES = [
    ('P', 'Personal'),
    ('B', 'Business')
]

class CustomUser(AbstractUser):
    # 額外欄位
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    country = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return self.username

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.account_number} - {self.user.username}'

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('W', 'Withdraw'),
        ('D', 'Deposit'),
        ('T', 'Transfer')
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    recipient_account = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount} - {self.account}'

