from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Wallets(models.Model):
    """
    ORM model for wallet table
    """

    id = models.AutoField
    name = models.CharField(max_length=20, unique=True, null=False)
    balance = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0"))],
        null=False,
    )


class TransactionLogs(models.Model):
    """
    ORM model for Log table
    """

    id = models.AutoField
    wallet = models.ForeignKey("Wallets", on_delete=models.CASCADE, null=False)
    OPERATION_TYPE = (
        ("c", "Create"),
        ("d", "Deposit"),
        ("w", "Withdrawal"),
        ("r", "Receive"),
        ("s", "Send"),
    )
    operation = models.CharField(max_length=1, choices=OPERATION_TYPE, null=False)
    amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0"))],
        null=False,
    )
    date = models.DateTimeField(null=False)
    sender = models.IntegerField(null=True, blank=True)
    recipient = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["date"]
