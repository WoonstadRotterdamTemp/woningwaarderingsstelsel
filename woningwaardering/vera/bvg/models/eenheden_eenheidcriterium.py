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

class EenhedenEenheidcriterium(BaseModel):
    """
    EenhedenEenheidcriterium
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    soort: Optional[Referentiedata] = Field(None, description="Het soort criterium. Bijv. Binding, Groep, Indicatie, Urgentie. Referentiedatasoort EENHEIDCRITERIUMSOORT.")
    detailsoort: Optional[Referentiedata] = Field(None, description="Het soort criterium op basis waarvan de woning passend is of waarop men voorang kan krijgen. Referentiedatasoort EENHEIDCRITERIUMDETAILSOORT.")
    aantal_bovengrens: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="aantalBovengrens", description="Bovengrens, waarbij de eenheid van deze grootheid afhankelijk is van de soort regel, bijvoorbeeld personen, euro's, meters, etc.")
    aantal_exact: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="aantalExact", description="De exacte waarde. De eenheid van deze grootheid is afhankelijk van de soort regel, bijvoorbeeld personen, euro's, vierkante meters, etc.")
    aantal_ondergrens: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="aantalOndergrens", description="Ondergrens, waarbij de eenheid van deze grootheid afhankelijk is van de soort regel, bijvoorbeeld personen, euro's of vierkante meters.")
    doelgroep: Optional[Referentiedata] = Field(None, description="De doelgroep waarop het criterium van toepassing is. Referentiedatasoort DOELGROEP.")
    toepassing: Optional[Referentiedata] = Field(None, description="Of het een selectie- of sorteercriterium betreft. Referentiedatasoort EENHEIDCRITERIUMTOEPASSING.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "soort", "detailsoort", "aantalBovengrens", "aantalExact", "aantalOndergrens", "doelgroep", "toepassing"]

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
    def from_json(cls, json_str: str) -> EenhedenEenheidcriterium:
        """Create an instance of EenhedenEenheidcriterium from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of detailsoort
        if self.detailsoort:
            _dict['detailsoort'] = self.detailsoort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of doelgroep
        if self.doelgroep:
            _dict['doelgroep'] = self.doelgroep.to_dict()
        # override the default output from pydantic by calling `to_dict()` of toepassing
        if self.toepassing:
            _dict['toepassing'] = self.toepassing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EenhedenEenheidcriterium:
        """Create an instance of EenhedenEenheidcriterium from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EenhedenEenheidcriterium.parse_obj(obj)

        _obj = EenhedenEenheidcriterium.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "soort": Referentiedata.from_dict(obj.get("soort")) if obj.get("soort") is not None else None,
            "detailsoort": Referentiedata.from_dict(obj.get("detailsoort")) if obj.get("detailsoort") is not None else None,
            "aantal_bovengrens": obj.get("aantalBovengrens"),
            "aantal_exact": obj.get("aantalExact"),
            "aantal_ondergrens": obj.get("aantalOndergrens"),
            "doelgroep": Referentiedata.from_dict(obj.get("doelgroep")) if obj.get("doelgroep") is not None else None,
            "toepassing": Referentiedata.from_dict(obj.get("toepassing")) if obj.get("toepassing") is not None else None
        })
        return _obj


