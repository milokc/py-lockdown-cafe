from __future__ import annotations
import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe():
    def __init__(self: Cafe, name: str) -> None:
        self.name = name

    def visit_cafe(self: Cafe, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError()
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError()
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"
