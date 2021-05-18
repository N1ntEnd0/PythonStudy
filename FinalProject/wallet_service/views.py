import json
from decimal import Decimal
from json import JSONDecodeError

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.utils import timezone

from . import models


def create_wallet(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            name = data.get("name")
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        if not models.Wallets.objects.filter(name=name).exists() and len(name) <= 20:
            try:
                with transaction.atomic():
                    wallet = models.Wallets.objects.create(
                        name=name, balance=0
                    ).full_clean()
                    models.TransactionLogs.objects.create(
                        wallet_id=wallet.id,
                        operation="c",
                        amount=wallet.balance,
                        date=timezone.now(),
                    ).full_clean()
                    return HttpResponse(status=201)
            except ValidationError:
                return HttpResponse(status=409)
    return HttpResponse(status=400)


def deposit(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            name = data.get("name")
            value = Decimal(data.get("balance"))
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        if models.Wallets.objects.filter(name=name).exists() and value >= 0.01:
            try:
                with transaction.atomic():
                    models.Wallets.objects.filter(name=name).update(
                        balance=F("balance") + value
                    )
                    wallet = models.Wallets.objects.get(name=name)
                    wallet.full_clean()
                    models.TransactionLogs.objects.create(
                        wallet_id=wallet.id,
                        operation="d",
                        amount=value,
                        date=timezone.now(),
                    ).full_clean()
                return HttpResponse(status=204)
            except ValidationError as e:
                return HttpResponse(status=400)
    return HttpResponse(status=400)


def money_transfer(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            sender = data.get("sender")
            recipient = data.get("recipient")
            value = Decimal(data.get("amount"))
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        sen_wallet = models.Wallets.objects.filter(name=sender)
        rec_wallet = models.Wallets.objects.filter(name=recipient)
        if value >= 0.01 and sen_wallet.exists() and rec_wallet.exists():
            try:
                with transaction.atomic():
                    sen_wallet.update(balance=F("balance") - value)
                    sen_wallet.get(name=sender).full_clean()
                    rec_wallet.update(balance=F("balance") + value).full_clean()
                    rec_wallet.get(name=recipient).full_clean()
                    models.TransactionLogs.objects.create(
                        wallet_id=sen_wallet.values("id"),
                        operation="s",
                        amount=value,
                        date=timezone.now(),
                        recipient=rec_wallet.values("id"),
                    ).full_clean()
                    models.TransactionLogs.objects.create(
                        wallet_id=rec_wallet.values("id"),
                        operation="r",
                        amount=value,
                        date=timezone.now(),
                        sender=sen_wallet.values("id"),
                    ).full_clean()
                    return HttpResponse(status=204)
            except ValidationError:
                return HttpResponse(status=409)
    return HttpResponse(status=400)


def get_wallets(request):
    if request.method == "GET":
        data = list(models.Wallets.objects.all().values("name", "balance"))
        return HttpResponse(json.dumps(data, default=str), status=200)
    return HttpResponse(status=400)


def get_logs(request):
    if request.method == "GET":
        try:
            name = request.GET.get("name")
        except TypeError:
            return HttpResponse(status=400)
        wall_id = models.Wallets.objects.filter(name=name)
        if wall_id.exists():
            data = list(
                models.TransactionLogs.objects.filter(
                    wallet_id=wall_id.values_list("id")[0]
                ).values(
                    "amount", "date", "sender", "recipient", "wallet_id", "operation"
                )
            )
            return HttpResponse(json.dumps(data, default=str), status=200)
    return HttpResponse(status=400)
