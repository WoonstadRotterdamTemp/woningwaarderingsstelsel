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

from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from woningwaardering.vera.bvg.models.eenheid_sleutels import EenheidSleutels
from woningwaardering.vera.bvg.models.extra_attribuut import ExtraAttribuut
from woningwaardering.vera.bvg.models.informatieobject import Informatieobject
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata
from woningwaardering.vera.bvg.models.sturingslabel import Sturingslabel
from woningwaardering.vera.bvg.models.woningwaardering_resultaten_woningwaardering_groep import WoningwaarderingResultatenWoningwaarderingGroep

class WoningwaarderingResultatenWoningwaarderingResultaatbericht(BaseModel):
    """
    WoningwaarderingResultatenWoningwaarderingResultaatbericht
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    begindatum: Optional[date] = Field(None, description="De begindatum van de woningwaardering puntentotaal.")
    einddatum: Optional[date] = Field(None, description="De einddatum waarop de waarop de woningwaardering niet meer geldig is.")
    eenheid: Optional[EenheidSleutels] = Field(None, description="De eenheid behorend bij de woningwaardering.")
    groepen: Optional[conlist(WoningwaarderingResultatenWoningwaarderingGroep)] = Field(None, description="De woningwaarderingenGroep behorend bij het woningwaardering puntentotaal.")
    maximale_huur: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maximaleHuur", description="De maximaal redelijke huur in euro's die geregistreerd staat bij de eenheid. De maximale huur is de huurprijs die gevraagd kan worden voor de eenheid op basis van de woningwaarderingspunten.")
    opslagpercentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Het percentage dat boven de maximale huurprijs op basis van punten mag worden gerekend. Bijvoorbeeld bij specifieke monumenten binnen stads of dorpsgezichten van voor 1945 waarbij de corporatie extra onderhoud pleegt aan het monument.")
    punten: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Het aantal woningwaarderingsstelsel punten dat is toegekend.")
    stelsel: Optional[Referentiedata] = Field(None, description="Het woningwaardering stelsel geeft aan welk puntensysteem voor de eenheid van toepassing is: het puntensysteem voor zelfstandige woonruimten, het puntensysteem voor onzelfstandige woonruimten, of het puntensysteem voor woonwagens en standplaatsen. Referentiedatasoort WONINGWAARDERINGSTELSEL.")
    extra_attributen: Optional[conlist(ExtraAttribuut)] = Field(None, alias="extra-attributen", description="Mogelijkheid om het bericht uit te breiden met attributen die nog niet in het logisch datamodel beschikbaar zijn")
    informatieobjecten: Optional[conlist(Informatieobject)] = Field(None, description="Mogelijkheid om het bericht uit te breiden met documentatie. De beschrijving kan de inhoud van een notitie of memo zijn")
    sturingslabels: Optional[conlist(Sturingslabel)] = Field(None, description="Mogelijkheid om het bericht uit te breiden met sturingslabels")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "begindatum", "einddatum", "eenheid", "groepen", "maximaleHuur", "opslagpercentage", "punten", "stelsel", "extra-attributen", "informatieobjecten", "sturingslabels"]

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
    def from_json(cls, json_str: str) -> WoningwaarderingResultatenWoningwaarderingResultaatbericht:
        """Create an instance of WoningwaarderingResultatenWoningwaarderingResultaatbericht from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of eenheid
        if self.eenheid:
            _dict['eenheid'] = self.eenheid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groepen (list)
        _items = []
        if self.groepen:
            for _item in self.groepen:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groepen'] = _items
        # override the default output from pydantic by calling `to_dict()` of stelsel
        if self.stelsel:
            _dict['stelsel'] = self.stelsel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in extra_attributen (list)
        _items = []
        if self.extra_attributen:
            for _item in self.extra_attributen:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extra-attributen'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in informatieobjecten (list)
        _items = []
        if self.informatieobjecten:
            for _item in self.informatieobjecten:
                if _item:
                    _items.append(_item.to_dict())
            _dict['informatieobjecten'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sturingslabels (list)
        _items = []
        if self.sturingslabels:
            for _item in self.sturingslabels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sturingslabels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WoningwaarderingResultatenWoningwaarderingResultaatbericht:
        """Create an instance of WoningwaarderingResultatenWoningwaarderingResultaatbericht from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WoningwaarderingResultatenWoningwaarderingResultaatbericht.parse_obj(obj)

        _obj = WoningwaarderingResultatenWoningwaarderingResultaatbericht.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "begindatum": obj.get("begindatum"),
            "einddatum": obj.get("einddatum"),
            "eenheid": EenheidSleutels.from_dict(obj.get("eenheid")) if obj.get("eenheid") is not None else None,
            "groepen": [WoningwaarderingResultatenWoningwaarderingGroep.from_dict(_item) for _item in obj.get("groepen")] if obj.get("groepen") is not None else None,
            "maximale_huur": obj.get("maximaleHuur"),
            "opslagpercentage": obj.get("opslagpercentage"),
            "punten": obj.get("punten"),
            "stelsel": Referentiedata.from_dict(obj.get("stelsel")) if obj.get("stelsel") is not None else None,
            "extra_attributen": [ExtraAttribuut.from_dict(_item) for _item in obj.get("extra-attributen")] if obj.get("extra-attributen") is not None else None,
            "informatieobjecten": [Informatieobject.from_dict(_item) for _item in obj.get("informatieobjecten")] if obj.get("informatieobjecten") is not None else None,
            "sturingslabels": [Sturingslabel.from_dict(_item) for _item in obj.get("sturingslabels")] if obj.get("sturingslabels") is not None else None
        })
        return _obj


