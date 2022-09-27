from enum import Enum


class AccountType(str, Enum):
    FREE = "free"
    PREMIUM = "premium"

    def __repr__(self):
        return self.value
    