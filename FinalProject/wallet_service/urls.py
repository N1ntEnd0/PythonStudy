from django.urls import path

from . import views

urlpatterns = [
    path("allWallets", views.get_wallets),
    path("create", views.create_wallet),
    path("deposit", views.deposit),
    path("transfer", views.money_transfer),
    path("logs", views.get_logs),
]
