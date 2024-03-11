# coding: utf-8

"""
    VERA-Beheer Vastgoedgegevens

    API-specificatie van ketenproces 'Beheer Vastgoedgegevens'. Deze specificatie is gebaseerd op VERA versie 4.1.4+240311.2

    The version of the OpenAPI document: 1.1.4+240311.2
    Contact: VERA@aedesdatastandaarden.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from woningwaardering.vera.bvg.models.bouwkundig_elementen_rechtspersoon import BouwkundigElementenRechtspersoon
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

BOUWKUNDIGELEMENTENRELATIE_ONE_OF_SCHEMAS = ["BouwkundigElementenRechtspersoon"]

class BouwkundigElementenRelatie(BaseModel):
    """
    BouwkundigElementenRelatie
    """
    # data type: BouwkundigElementenRechtspersoon
    oneof_schema_1_validator: Optional[BouwkundigElementenRechtspersoon] = None
    if TYPE_CHECKING:
        actual_instance: Union[BouwkundigElementenRechtspersoon]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(BOUWKUNDIGELEMENTENRELATIE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = BouwkundigElementenRelatie.construct()
        error_messages = []
        match = 0
        # validate data type: BouwkundigElementenRechtspersoon
        if not isinstance(v, BouwkundigElementenRechtspersoon):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BouwkundigElementenRechtspersoon`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BouwkundigElementenRelatie with oneOf schemas: BouwkundigElementenRechtspersoon. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BouwkundigElementenRelatie with oneOf schemas: BouwkundigElementenRechtspersoon. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> BouwkundigElementenRelatie:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> BouwkundigElementenRelatie:
        """Returns the object represented by the json string"""
        instance = BouwkundigElementenRelatie.construct()
        error_messages = []
        match = 0

        # deserialize data into BouwkundigElementenRechtspersoon
        try:
            instance.actual_instance = BouwkundigElementenRechtspersoon.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BouwkundigElementenRelatie with oneOf schemas: BouwkundigElementenRechtspersoon. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BouwkundigElementenRelatie with oneOf schemas: BouwkundigElementenRechtspersoon. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


