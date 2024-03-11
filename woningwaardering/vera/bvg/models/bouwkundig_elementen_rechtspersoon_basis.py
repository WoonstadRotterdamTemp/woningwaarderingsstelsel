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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from woningwaardering.vera.bvg.models.bouwkundig_elementen_relatierol import BouwkundigElementenRelatierol
from woningwaardering.vera.bvg.models.contactgegeven_sleutels import ContactgegevenSleutels
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata
from woningwaardering.vera.bvg.models.relatie_sleutels import RelatieSleutels

class BouwkundigElementenRechtspersoonBasis(BaseModel):
    """
    BouwkundigElementenRechtspersoonBasis
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    soort: Optional[Referentiedata] = Field(None, description="Het soort relatie: NatuurlijkPersoon, Relatiegroep of Rechtspersoon. Referentiedatasoort RELATIESOORT.")
    detail_soort: Optional[Referentiedata] = Field(None, alias="detailSoort", description="Het detail van soort relatie: Bijvoorbeeld Huishouden bij een relatiegroep, of de standaard bedrijfsindeling volgens SBI bij een rechtspersoon. Referentiedatasoort RELATIEDETAILSOORT.")
    contactgegevens: Optional[conlist(ContactgegevenSleutels)] = Field(None, description="De contactgegevens van de relatie.")
    relaties: Optional[conlist(RelatieSleutels)] = Field(None, description="De gerelateerde relaties. Bijv. contactpersonen, huishoudleden etc.")
    rollen: Optional[conlist(BouwkundigElementenRelatierol)] = Field(None, description="De rollen behorend bij de relatie. Bijvoorbeeld: Prospect, bewoner.")
    globaal_locatienummer: Optional[StrictStr] = Field(None, alias="globaalLocatienummer", description="Een wereldwijd nummer ter identificatie van een partij of locatie. Het dertiencijferige nummer (GLN) wordt uitgegeven door GS1.")
    naam: Optional[StrictStr] = Field(None, description="De naam de rechtspersoon.")
    btw_nummer: Optional[StrictStr] = Field(None, alias="btwNummer", description="Het BTW nummer van de rechtspersoon.")
    kvk_nummer: Optional[StrictStr] = Field(None, alias="kvkNummer", description="Het KVK nummer van de rechtspersoon.")
    organisatievorm: Optional[Referentiedata] = Field(None, description="De organisatievorm van de rechtspersoon. Bijvoorbeeld: BV, NV, stichting of vereniging. Ook wel rechtsvorm genoemd. Referentiedatasoort ORGANISATIEVORM.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "soort", "detailSoort", "contactgegevens", "relaties", "rollen", "globaalLocatienummer", "naam", "btwNummer", "kvkNummer", "organisatievorm"]

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
    def from_json(cls, json_str: str) -> BouwkundigElementenRechtspersoonBasis:
        """Create an instance of BouwkundigElementenRechtspersoonBasis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contactgegevens (list)
        _items = []
        if self.contactgegevens:
            for _item in self.contactgegevens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contactgegevens'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in relaties (list)
        _items = []
        if self.relaties:
            for _item in self.relaties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relaties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rollen (list)
        _items = []
        if self.rollen:
            for _item in self.rollen:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rollen'] = _items
        # override the default output from pydantic by calling `to_dict()` of organisatievorm
        if self.organisatievorm:
            _dict['organisatievorm'] = self.organisatievorm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BouwkundigElementenRechtspersoonBasis:
        """Create an instance of BouwkundigElementenRechtspersoonBasis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BouwkundigElementenRechtspersoonBasis.parse_obj(obj)

        _obj = BouwkundigElementenRechtspersoonBasis.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "soort": Referentiedata.from_dict(obj.get("soort")) if obj.get("soort") is not None else None,
            "detail_soort": Referentiedata.from_dict(obj.get("detailSoort")) if obj.get("detailSoort") is not None else None,
            "contactgegevens": [ContactgegevenSleutels.from_dict(_item) for _item in obj.get("contactgegevens")] if obj.get("contactgegevens") is not None else None,
            "relaties": [RelatieSleutels.from_dict(_item) for _item in obj.get("relaties")] if obj.get("relaties") is not None else None,
            "rollen": [BouwkundigElementenRelatierol.from_dict(_item) for _item in obj.get("rollen")] if obj.get("rollen") is not None else None,
            "globaal_locatienummer": obj.get("globaalLocatienummer"),
            "naam": obj.get("naam"),
            "btw_nummer": obj.get("btwNummer"),
            "kvk_nummer": obj.get("kvkNummer"),
            "organisatievorm": Referentiedata.from_dict(obj.get("organisatievorm")) if obj.get("organisatievorm") is not None else None
        })
        return _obj


