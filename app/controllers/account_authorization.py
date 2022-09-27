import datetime

from flask_login import current_user
# from flask import redirect, url_for

from app.models import User
from config import BaseConfig


# def check_account_expiration(func):
#     user: User = current_user
#     if user and user.account_type == User.AccountType.FREE:
#         expiration_date = user.created_at + datetime.timedelta(days=BaseConfig.FREE_EXPIRATION_DAYS)
#         if expiration_date > datetime.datetime.now():
#             return func
#     elif user and user.subscription_due > datetime.datetime.now():
#         return func

#     def wrapped(*args, **kwargs):
#         if not current_user.is_authenticated:
#             return redirect(url_for("auth.login"))
#         return redirect(url_for("main.banner"))

#     return wrapped


def check_account_expiration():
    user: User = current_user
    if user.account_type == User.AccountType.FREE:
        expiration_date = user.created_at + datetime.timedelta(days=BaseConfig.FREE_EXPIRATION_DAYS)
        if expiration_date > datetime.datetime.now():
            return True
    elif user.subscribed_due > datetime.datetime.now():
        return True
    return False
