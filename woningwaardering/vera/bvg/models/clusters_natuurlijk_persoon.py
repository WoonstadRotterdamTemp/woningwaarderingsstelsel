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
from woningwaardering.vera.bvg.models.clusters_relatierol import ClustersRelatierol
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata
from woningwaardering.vera.bvg.models.relatie_sleutels import RelatieSleutels

class ClustersNatuurlijkPersoon(BaseModel):
    """
    ClustersNatuurlijkPersoon
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    soort: Optional[Referentiedata] = Field(None, description="Het soort relatie: NatuurlijkPersoon, Relatiegroep of Rechtspersoon. Referentiedatasoort RELATIESOORT.")
    detail_soort: Optional[Referentiedata] = Field(None, alias="detailSoort", description="Het detail van soort relatie: Bijvoorbeeld Huishouden bij een relatiegroep, of de standaard bedrijfsindeling volgens SBI bij een rechtspersoon. Referentiedatasoort RELATIEDETAILSOORT.")
    relaties: Optional[conlist(RelatieSleutels)] = Field(None, description="De gerelateerde relaties. Bijv. contactpersonen, huishoudleden etc.")
    rollen: Optional[conlist(ClustersRelatierol)] = Field(None, description="De rollen behorend bij de relatie. Bijvoorbeeld: Prospect, bewoner.")
    aanhef: Optional[StrictStr] = Field(None, description="De aanhef of aanspreking is een (meestal vriendelijke) introducerende zin van een brief of e-mail. Het gaat doorgaans om standaardformuleringen waarmee de schrijver zich tot de geadresseerde richt.")
    aanschrijfnaam: Optional[StrictStr] = Field(None, description="De achternaam van de natuurlijk persoon zoals deze wenst te worden aangeschreven.")
    achternaam: Optional[StrictStr] = Field(None, description="De achternaam van de natuurlijk persoon.")
    initialen: Optional[StrictStr] = Field(None, description="De initialen van de natuurlijk persoon.")
    roepnaam: Optional[StrictStr] = Field(None, description="De roepnaam van de natuurlijk persoon.")
    tussenvoegsels: Optional[StrictStr] = Field(None, description="De tussenvoegsels behorende bij de naam.")
    voorletters: Optional[StrictStr] = Field(None, description="Een voorletter is een afkorting van een voornaam, die in adressering veel wordt gebruikt. De voorletters geven in combinatie met de achternaam meestal een duidelijk onderscheid tussen leden van hetzelfde gezin of dezelfde familie. Indien iemand meerdere voornamen heeft dan worden de voorletters door een punt gescheiden.")
    voornaam: Optional[StrictStr] = Field(None, description="De voornaam van de natuurlijk persoon.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "soort", "detailSoort", "relaties", "rollen", "aanhef", "aanschrijfnaam", "achternaam", "initialen", "roepnaam", "tussenvoegsels", "voorletters", "voornaam"]

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
    def from_json(cls, json_str: str) -> ClustersNatuurlijkPersoon:
        """Create an instance of ClustersNatuurlijkPersoon from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClustersNatuurlijkPersoon:
        """Create an instance of ClustersNatuurlijkPersoon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClustersNatuurlijkPersoon.parse_obj(obj)

        _obj = ClustersNatuurlijkPersoon.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "soort": Referentiedata.from_dict(obj.get("soort")) if obj.get("soort") is not None else None,
            "detail_soort": Referentiedata.from_dict(obj.get("detailSoort")) if obj.get("detailSoort") is not None else None,
            "relaties": [RelatieSleutels.from_dict(_item) for _item in obj.get("relaties")] if obj.get("relaties") is not None else None,
            "rollen": [ClustersRelatierol.from_dict(_item) for _item in obj.get("rollen")] if obj.get("rollen") is not None else None,
            "aanhef": obj.get("aanhef"),
            "aanschrijfnaam": obj.get("aanschrijfnaam"),
            "achternaam": obj.get("achternaam"),
            "initialen": obj.get("initialen"),
            "roepnaam": obj.get("roepnaam"),
            "tussenvoegsels": obj.get("tussenvoegsels"),
            "voorletters": obj.get("voorletters"),
            "voornaam": obj.get("voornaam")
        })
        return _obj


