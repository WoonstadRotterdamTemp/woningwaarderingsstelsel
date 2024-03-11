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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata

class EenhedenRuimte(BaseModel):
    """
    EenhedenRuimte
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    soort: Optional[Referentiedata] = Field(None, description="Het soort ruimte. Ruimtes worden verdeeld in vertrekken die meetellen voor de woningwaardering, buitenruimtes en overige ruimtes. Referentiedatasoort RUIMTESOORT.")
    detail_soort: Optional[Referentiedata] = Field(None, alias="detailSoort", description="Het detailsoort van de ruimte. Bijv. Slaapkamer, Dakteras, Tuin etc. Referentiedatasoort RUIMTEDETAILSOORT.")
    naam: Optional[StrictStr] = Field(None, description="De omschrijving van de ruimte.")
    inhoud: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="De inhoud van de ruimte in m3.")
    ligging: Optional[Referentiedata] = Field(None, description="De ligging van de ruimte. Referentiedatasoort RUIMTELIGGING.")
    oppervlakte: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="De oppervlakte van de ruimte")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "soort", "detailSoort", "naam", "inhoud", "ligging", "oppervlakte"]

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
    def from_json(cls, json_str: str) -> EenhedenRuimte:
        """Create an instance of EenhedenRuimte from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of soort
        if self.soort:
            _dict['soort'] = self.soort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of detail_soort
        if self.detail_soort:
            _dict['detailSoort'] = self.detail_soort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ligging
        if self.ligging:
            _dict['ligging'] = self.ligging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EenhedenRuimte:
        """Create an instance of EenhedenRuimte from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EenhedenRuimte.parse_obj(obj)

        _obj = EenhedenRuimte.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "soort": Referentiedata.from_dict(obj.get("soort")) if obj.get("soort") is not None else None,
            "detail_soort": Referentiedata.from_dict(obj.get("detailSoort")) if obj.get("detailSoort") is not None else None,
            "naam": obj.get("naam"),
            "inhoud": obj.get("inhoud"),
            "ligging": Referentiedata.from_dict(obj.get("ligging")) if obj.get("ligging") is not None else None,
            "oppervlakte": obj.get("oppervlakte")
        })
        return _obj


