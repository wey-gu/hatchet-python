# coding: utf-8

"""
    Hatchet API

    The Hatchet API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from hatchet_sdk.clients.rest.models.api_resource_meta import APIResourceMeta
from hatchet_sdk.clients.rest.models.github_app_installation import (
    GithubAppInstallation,
)


class WorkflowDeploymentConfig(BaseModel):
    """
    WorkflowDeploymentConfig
    """  # noqa: E501

    metadata: APIResourceMeta
    git_repo_name: StrictStr = Field(
        description="The repository name.", alias="gitRepoName"
    )
    git_repo_owner: StrictStr = Field(
        description="The repository owner.", alias="gitRepoOwner"
    )
    git_repo_branch: StrictStr = Field(
        description="The repository branch.", alias="gitRepoBranch"
    )
    github_app_installation: Optional[GithubAppInstallation] = Field(
        default=None,
        description="The Github App installation.",
        alias="githubAppInstallation",
    )
    github_app_installation_id: StrictStr = Field(
        description="The id of the Github App installation.",
        alias="githubAppInstallationId",
    )
    __properties: ClassVar[List[str]] = [
        "metadata",
        "gitRepoName",
        "gitRepoOwner",
        "gitRepoBranch",
        "githubAppInstallation",
        "githubAppInstallationId",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkflowDeploymentConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of github_app_installation
        if self.github_app_installation:
            _dict["githubAppInstallation"] = self.github_app_installation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkflowDeploymentConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "metadata": (
                    APIResourceMeta.from_dict(obj["metadata"])
                    if obj.get("metadata") is not None
                    else None
                ),
                "gitRepoName": obj.get("gitRepoName"),
                "gitRepoOwner": obj.get("gitRepoOwner"),
                "gitRepoBranch": obj.get("gitRepoBranch"),
                "githubAppInstallation": (
                    GithubAppInstallation.from_dict(obj["githubAppInstallation"])
                    if obj.get("githubAppInstallation") is not None
                    else None
                ),
                "githubAppInstallationId": obj.get("githubAppInstallationId"),
            }
        )
        return _obj
