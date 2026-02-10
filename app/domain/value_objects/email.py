import re

class Email:
    _EMAIL_REGEX = re.compile(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

    def __init__(self, value: str):
        if not value:
            raise ValueError("Email is required")

        value = value.strip().lower()

        if not self._EMAIL_REGEX.match(value):
            raise ValueError("Invalid email format")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        if not isinstance(other, Email):
            return False
        return self._value == other._value

    def __str__(self) -> str:
        return self._value


    