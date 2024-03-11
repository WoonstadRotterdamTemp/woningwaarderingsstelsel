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
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from woningwaardering.vera.bvg.models.eenheden_stadsdeel import EenhedenStadsdeel

class EenhedenWijk(BaseModel):
    """
    EenhedenWijk
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    naam: Optional[StrictStr] = Field(None, description="De naam van de wijk.")
    stadsdeel: Optional[EenhedenStadsdeel] = Field(None, description="Het stadsdeel van de wijk.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "naam", "stadsdeel"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EenhedenWijk:
        """Create an instance of EenhedenWijk from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of stadsdeel
        if self.stadsdeel:
            _dict['stadsdeel'] = self.stadsdeel.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EenhedenWijk:
        """Create an instance of EenhedenWijk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EenhedenWijk.parse_obj(obj)

        _obj = EenhedenWijk.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "naam": obj.get("naam"),
            "stadsdeel": EenhedenStadsdeel.from_dict(obj.get("stadsdeel")) if obj.get("stadsdeel") is not None else None
        })
        return _obj


