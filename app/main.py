from __future__ import annotations
import datetime
from cafe import Cafe
from  errors import NotWearingMaskError, VaccineError

# class VaccineError(Exception):
#     pass


# class NotVaccinatedError(VaccineError):
#     pass


# class OutdatedVaccineError(VaccineError):
#     pass


# class NotWearingMaskError(Exception):
#     pass


# class Cafe():
#     def __init__(self: "Cafe", name: str) -> None:
#         self.name = name

#     def visit_cafe(self: "Cafe", visitor: dict) -> str:
#         if visitor.get("vaccine") is None:
#             raise NotVaccinatedError()
#         elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
#             raise OutdatedVaccineError()
#         elif not visitor["wearing_a_mask"]:
#             raise NotWearingMaskError()
#         else:
#             return f"Welcome to {self.name}"


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        for friend in friends:
            if not friend["wearing_a_mask"]:
                masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"

friends = [
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    },
]
print(go_to_cafe(friends, Cafe("KFC"))) == "Friends should buy 2 masks"