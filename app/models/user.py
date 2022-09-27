import datetime
from enum import Enum

from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models.utils import ModelMixin
from config import BaseConfig


class User(db.Model, UserMixin, ModelMixin):
    class AccountType(str, Enum):
        FREE = "free"
        PREMIUM = "premium"

        def __repr__(self):
            return self.value

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    account_type = db.Column(db.Enum(AccountType), default=AccountType.FREE)
    subscribed_due = db.Column(db.DateTime,
                               default=datetime.datetime.now() +
                                       datetime.timedelta(days=BaseConfig.FREE_EXPIRATION_DAYS))
    activated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def authenticate(cls, user_id, password):
        user = cls.query.filter(
            db.or_(func.lower(cls.username) == func.lower(user_id), func.lower(cls.email) == func.lower(user_id))
        ).first()
        if user is not None and check_password_hash(user.password, password):
            return user

    def __repr__(self):
        return f"<User: {self.username}>"


class AnonymousUser(AnonymousUserMixin):
    pass
