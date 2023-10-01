# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from petstore_api.models.tag import Tag

class MapOfArrayOfModel(BaseModel):
    """
    MapOfArrayOfModel
    """
    shop_id_to_org_online_lip_map: Optional[Dict[str, List[Tag]]] = Field(default=None, alias="shopIdToOrgOnlineLipMap")
    __properties: ClassVar[List[str]] = ["shopIdToOrgOnlineLipMap"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MapOfArrayOfModel:
        """Create an instance of MapOfArrayOfModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in shop_id_to_org_online_lip_map (dict of array)
        _field_dict_of_array = {}
        if self.shop_id_to_org_online_lip_map:
            for _key in self.shop_id_to_org_online_lip_map:
                if self.shop_id_to_org_online_lip_map[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.shop_id_to_org_online_lip_map[_key]
                    ]
            _dict['shopIdToOrgOnlineLipMap'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapOfArrayOfModel:
        """Create an instance of MapOfArrayOfModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapOfArrayOfModel.model_validate(obj)

        _obj = MapOfArrayOfModel.model_validate({
            "shopIdToOrgOnlineLipMap": dict(
                (_k,
                        [Tag.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("shopIdToOrgOnlineLipMap").items()
            )
        })
        return _obj


