from enum import Enum


class Criteria(str, Enum):
    SUPPLIER = "SUPPLIER"
    CODE = "CODE"
    DESCRIPTION = "DESCRIPTION"
    YEAR = "YEAR"
    BRAND = "BRAND"

    def get_str(self):
        return self.name.lower()
