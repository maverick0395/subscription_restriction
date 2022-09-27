from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


class SubscriptionForm(FlaskForm):
    plan_type = RadioField("subscription_plan_type", choices=[(30, "Monthly Plan"),(365, "Annual Plan")])
    submit = SubmitField("Subscribe")
