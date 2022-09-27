import datetime

from flask import redirect, render_template, url_for, Blueprint, request
from flask_login import login_required, current_user

from app.forms import SubscriptionForm
from app.models import User
from app.services import AccountService


subscription_blueprint = Blueprint("subscription", __name__)


@subscription_blueprint.route("/update", methods=["GET", "POST"])
@login_required
def update():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    user: User = current_user
    account_service: AccountService = AccountService()
    form: SubscriptionForm = SubscriptionForm(request.form)

    if form.validate_on_submit():
        update_data = {"subscribed_due": datetime.datetime.now() + datetime.timedelta(days=int(form.plan_type.data)), "account_type": User.AccountType.PREMIUM}
        account_service.update(id=user.id, **update_data)

        return render_template("index.html")

    return render_template("banner.html", form=form)
