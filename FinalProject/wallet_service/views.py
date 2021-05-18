import json
from decimal import Decimal
from json import JSONDecodeError

from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.db.models import F, QuerySet
from django.http import HttpResponse
from django.utils import timezone

from . import models
from .models import Wallets


def create_wallet(request: WSGIRequest) -> HttpResponse:
    """
    The method processes the POST request and creates a new wallet.

    :param request:
        WSGIRequest
    :return:
        HttpResponse
    """
    if request.method == "POST":
        try:
            data: dict = json.loads(request.body)
            name: str = data.get("name")
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        if not models.Wallets.objects.filter(name=name).exists() and len(name) <= 20:
            try:
                with transaction.atomic():
                    wallet: Wallets = models.Wallets.objects.create(
                        name=name, balance=0
                    )
                    wallet.full_clean()

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


def deposit(request: WSGIRequest) -> HttpResponse:
    """
    The method validates the data and increases balance

    :param request:
        WSGIRequest
    :return:
        HttpResponse
    """
    if request.method == "PUT":

        try:
            data: dict = json.loads(request.body)
            name: str = data.get("name")
            value: Decimal = Decimal(data.get("balance"))
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        if models.Wallets.objects.filter(name=name).exists() and value >= 0.01:
            try:
                with transaction.atomic():
                    models.Wallets.objects.filter(name=name).update(
                        balance=F("balance") + value
                    )
                    wallet: Wallets = models.Wallets.objects.get(name=name)
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


def money_transfer(request: WSGIRequest) -> HttpResponse:
    """
    The method validates data and transfers money between two wallets.

    :param request:
        WSGIRequest
    :return:
        HttpResponse
    """
    if request.method == "PUT":

        try:
            data: dict = json.loads(request.body)
            sender: str = data.get("sender")
            recipient: str = data.get("recipient")
            value: Decimal = Decimal(data.get("amount"))
        except JSONDecodeError or TypeError:
            return HttpResponse(status=400)

        sen_wallet: QuerySet = models.Wallets.objects.filter(name=sender)
        rec_wallet: QuerySet = models.Wallets.objects.filter(name=recipient)
        if value >= 0.01 and sen_wallet.exists() and rec_wallet.exists():
            try:
                with transaction.atomic():
                    sen_wallet.update(balance=F("balance") - value)
                    sen: Wallets = sen_wallet.get(name=sender)
                    sen.full_clean()

                    rec_wallet.update(balance=F("balance") + value)
                    rec: Wallets = rec_wallet.get(name=recipient)
                    rec.full_clean()

                    models.TransactionLogs.objects.create(
                        wallet_id=sen.id,
                        operation="s",
                        amount=value,
                        date=timezone.now(),
                        recipient=rec.id,
                    ).full_clean()
                    models.TransactionLogs.objects.create(
                        wallet_id=rec.id,
                        operation="r",
                        amount=value,
                        date=timezone.now(),
                        sender=sen.id,
                    ).full_clean()
                    return HttpResponse(status=204)
            except ValidationError:
                return HttpResponse(status=409)
    return HttpResponse(status=400)


def get_wallets(request: WSGIRequest) -> HttpResponse:
    """
    The method returns information about all wallets in JSON format.

    :param request:
        WSGIRequest
    :return:
        HttpResponse with nested JSON
    """
    if request.method == "GET":
        data: list = list(models.Wallets.objects.all().values("name", "balance"))
        return HttpResponse(json.dumps(data, default=str), status=200)
    return HttpResponse(status=400)


def get_logs(request: WSGIRequest) -> HttpResponse:
    """
    The method returns operation log about selected wallet.

    :param request:
        WSGIRequest
    :return:
        HttpResponse with nested JSON
    """
    if request.method == "GET":
        try:
            name: str = request.GET.get("name")
        except TypeError:
            return HttpResponse(status=400)
        wall_id: QuerySet = models.Wallets.objects.filter(name=name)
        if wall_id.exists():
            data: list = list(
                models.TransactionLogs.objects.filter(
                    wallet_id=wall_id.values_list("id")[0]
                ).values("amount", "date", "sender", "recipient", "operation")
            )
            return HttpResponse(json.dumps(data, default=str), status=200)
    return HttpResponse(status=400)
