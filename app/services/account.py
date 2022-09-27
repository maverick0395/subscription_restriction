from app import db
from app.models import User


class AccountService:
    model = User

    def commit(self):
        try:
            db.session.commit()
        except Exception as error:
            raise error

    def update(self, id: int, **kwargs):
        try:
            instance: self.model = self.model.query.filter_by(id=id).all()[0]
            for attr, new_value in kwargs.items():
                setattr(instance, attr, new_value)
            self.commit()
        except Exception as error:
            raise error
