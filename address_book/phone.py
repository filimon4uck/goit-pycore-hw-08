from field import Field
import re


class Phone(Field):
    def __init__(self, phone):
        if not re.match(r'^\d{10}$', phone):
            raise ValueError("The phone number must be 10 digits")
        super().__init__(phone)
    
    def __repr__(self) -> str:
        return super().__repr__()

