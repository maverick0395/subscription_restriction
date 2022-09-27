from flask import redirect, render_template, url_for, Blueprint
from flask_login import login_required

from app.controllers import check_account_expiration


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@login_required
# @check_account_expiration
def index():
    if check_account_expiration():
        return render_template("index.html")
    else:
        return redirect(url_for("subscription.update"))


