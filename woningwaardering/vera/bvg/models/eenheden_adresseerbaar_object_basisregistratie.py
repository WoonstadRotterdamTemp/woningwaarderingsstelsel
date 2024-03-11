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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from woningwaardering.vera.bvg.models.adres_sleutels import AdresSleutels
from woningwaardering.vera.bvg.models.eenheden_bag_pand import EenhedenBagPand
from woningwaardering.vera.bvg.models.geometrie_sleutels import GeometrieSleutels
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata

class EenhedenAdresseerbaarObjectBasisregistratie(BaseModel):
    """
    EenhedenAdresseerbaarObjectBasisregistratie
    """
    id: Optional[StrictStr] = Field(None, description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.")
    id_extern: Optional[StrictStr] = Field(None, alias="idExtern", description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.")
    id_gegevensbeheerder: Optional[StrictStr] = Field(None, alias="idGegevensbeheerder", description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.")
    id_organisatie: Optional[StrictStr] = Field(None, alias="idOrganisatie", description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.")
    id_administratie: Optional[StrictStr] = Field(None, alias="idAdministratie", description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.")
    code: Optional[StrictStr] = Field(None, description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)")
    bag_gebruikers_oppervlakte: Optional[StrictInt] = Field(None, alias="bagGebruikersOppervlakte", description="De gebruikersoppervlakte zoals in de BAG beschreven.")
    bag_gebruiksdoelen: Optional[conlist(Referentiedata)] = Field(None, alias="bagGebruiksdoelen", description="De categorisering van de gebruiksdoelen van het betreffende verblijfsobject, zoals dit formeel door de overheid als zodanig is toegestaan. Referentiedatasoort GEBRUIKERSDOEL.")
    bag_hoofdadres: Optional[AdresSleutels] = Field(None, alias="bagHoofdadres", description="Het hoofdadres van het adresseerbaar object uit de basisregistratie.")
    bag_identificatie: Optional[StrictStr] = Field(None, alias="bagIdentificatie", description="De unieke aanduiding van een adresseerbaar object. (standplaats, ligplaats, of verblijfsobject)")
    bag_in_onderzoek: Optional[StrictBool] = Field(None, alias="bagInOnderzoek", description="De aanduiding waarmee wordt aangegeven dat een onderzoek wordt uitgevoerd naar de juistheid van een of meerdere gegevens van het betreffende object.")
    bag_nevenadressen: Optional[conlist(AdresSleutels)] = Field(None, alias="bagNevenadressen", description="De adressen die gerelateerd zijn aan het adresseerbaar object uit de basisregistratie. Het hoofdadres maakt geen deel uit van deze collectie.")
    bag_officieel: Optional[StrictBool] = Field(None, alias="bagOfficieel", description="De aanduiding waarmee kan worden aangegeven dat een object in de basisregistratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname.")
    bag_oppervlakte_verblijfsobject: Optional[StrictInt] = Field(None, alias="bagOppervlakteVerblijfsobject", description="De gebruiksoppervlakte van een verblijfsobject in gehele vierkante meters.")
    bag_panden_basisregistratie: Optional[conlist(EenhedenBagPand)] = Field(None, alias="bagPandenBasisregistratie", description="De panden die gerelateerd zijn aan het adresseerbaar object uit de basisregistratie.")
    bag_status: Optional[StrictStr] = Field(None, alias="bagStatus", description="De fase van de levenscyclus van een standplaats, ligplaats of verblijfsobject waarin het betreffende object zich bevindt.")
    geometrie: Optional[GeometrieSleutels] = Field(None, description="De geometrie van het adresseerbaar object uit de basisregistratie.")
    __properties = ["id", "idExtern", "idGegevensbeheerder", "idOrganisatie", "idAdministratie", "code", "bagGebruikersOppervlakte", "bagGebruiksdoelen", "bagHoofdadres", "bagIdentificatie", "bagInOnderzoek", "bagNevenadressen", "bagOfficieel", "bagOppervlakteVerblijfsobject", "bagPandenBasisregistratie", "bagStatus", "geometrie"]

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
    def from_json(cls, json_str: str) -> EenhedenAdresseerbaarObjectBasisregistratie:
        """Create an instance of EenhedenAdresseerbaarObjectBasisregistratie from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bag_gebruiksdoelen (list)
        _items = []
        if self.bag_gebruiksdoelen:
            for _item in self.bag_gebruiksdoelen:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bagGebruiksdoelen'] = _items
        # override the default output from pydantic by calling `to_dict()` of bag_hoofdadres
        if self.bag_hoofdadres:
            _dict['bagHoofdadres'] = self.bag_hoofdadres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bag_nevenadressen (list)
        _items = []
        if self.bag_nevenadressen:
            for _item in self.bag_nevenadressen:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bagNevenadressen'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bag_panden_basisregistratie (list)
        _items = []
        if self.bag_panden_basisregistratie:
            for _item in self.bag_panden_basisregistratie:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bagPandenBasisregistratie'] = _items
        # override the default output from pydantic by calling `to_dict()` of geometrie
        if self.geometrie:
            _dict['geometrie'] = self.geometrie.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EenhedenAdresseerbaarObjectBasisregistratie:
        """Create an instance of EenhedenAdresseerbaarObjectBasisregistratie from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EenhedenAdresseerbaarObjectBasisregistratie.parse_obj(obj)

        _obj = EenhedenAdresseerbaarObjectBasisregistratie.parse_obj({
            "id": obj.get("id"),
            "id_extern": obj.get("idExtern"),
            "id_gegevensbeheerder": obj.get("idGegevensbeheerder"),
            "id_organisatie": obj.get("idOrganisatie"),
            "id_administratie": obj.get("idAdministratie"),
            "code": obj.get("code"),
            "bag_gebruikers_oppervlakte": obj.get("bagGebruikersOppervlakte"),
            "bag_gebruiksdoelen": [Referentiedata.from_dict(_item) for _item in obj.get("bagGebruiksdoelen")] if obj.get("bagGebruiksdoelen") is not None else None,
            "bag_hoofdadres": AdresSleutels.from_dict(obj.get("bagHoofdadres")) if obj.get("bagHoofdadres") is not None else None,
            "bag_identificatie": obj.get("bagIdentificatie"),
            "bag_in_onderzoek": obj.get("bagInOnderzoek"),
            "bag_nevenadressen": [AdresSleutels.from_dict(_item) for _item in obj.get("bagNevenadressen")] if obj.get("bagNevenadressen") is not None else None,
            "bag_officieel": obj.get("bagOfficieel"),
            "bag_oppervlakte_verblijfsobject": obj.get("bagOppervlakteVerblijfsobject"),
            "bag_panden_basisregistratie": [EenhedenBagPand.from_dict(_item) for _item in obj.get("bagPandenBasisregistratie")] if obj.get("bagPandenBasisregistratie") is not None else None,
            "bag_status": obj.get("bagStatus"),
            "geometrie": GeometrieSleutels.from_dict(obj.get("geometrie")) if obj.get("geometrie") is not None else None
        })
        return _obj


