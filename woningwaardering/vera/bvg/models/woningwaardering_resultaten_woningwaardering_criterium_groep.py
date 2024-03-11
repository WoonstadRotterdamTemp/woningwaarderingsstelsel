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
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata

class WoningwaarderingResultatenWoningwaarderingCriteriumGroep(BaseModel):
    """
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    naam: Optional[StrictStr] = Field(None, description="De naam van de groep.")
    omschrijving: Optional[StrictStr] = Field(None, description="De omschrijving van de groep.")
    stelsel: Optional[Referentiedata] = Field(None, description="Het woningwaardering stelsel bevat een apart puntensystemen voor de eenheidssoorten zelfstandige woningen, kamers, woonwagens en woonwagenstandplaatsen. Dit attribuut geeft het toe te passen puntensysteem aan. Referentiedatasoort WONINGWAARDERINGSTELSEL.")
    stelselgroep: Optional[Referentiedata] = Field(None, description="De naam van de groep binnen het woningwaarderingsstelsel, zoals beschreven in het Besluit huurprijzen woonruimte. Referentiedatasoort WONINGWAARDERINGSTELSELGROEP.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "naam", "omschrijving", "stelsel", "stelselgroep"]

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
    def from_json(cls, json_str: str) -> WoningwaarderingResultatenWoningwaarderingCriteriumGroep:
        """Create an instance of WoningwaarderingResultatenWoningwaarderingCriteriumGroep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of stelsel
        if self.stelsel:
            _dict['stelsel'] = self.stelsel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stelselgroep
        if self.stelselgroep:
            _dict['stelselgroep'] = self.stelselgroep.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WoningwaarderingResultatenWoningwaarderingCriteriumGroep:
        """Create an instance of WoningwaarderingResultatenWoningwaarderingCriteriumGroep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WoningwaarderingResultatenWoningwaarderingCriteriumGroep.parse_obj(obj)

        _obj = WoningwaarderingResultatenWoningwaarderingCriteriumGroep.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "naam": obj.get("naam"),
            "omschrijving": obj.get("omschrijving"),
            "stelsel": Referentiedata.from_dict(obj.get("stelsel")) if obj.get("stelsel") is not None else None,
            "stelselgroep": Referentiedata.from_dict(obj.get("stelselgroep")) if obj.get("stelselgroep") is not None else None
        })
        return _obj


