# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Dashboard(msrest.serialization.Model):
    """The shared dashboard resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param lenses: The dashboard lenses.
    :type lenses: dict[str, ~portal.models.DashboardLens]
    :param metadata: The dashboard metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'lenses': {'key': 'properties.lenses', 'type': '{DashboardLens}'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        lenses: Optional[Dict[str, "DashboardLens"]] = None,
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(Dashboard, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
        self.lenses = lenses
        self.metadata = metadata


class DashboardLens(msrest.serialization.Model):
    """A dashboard lens.

    All required parameters must be populated in order to send to Azure.

    :param order: Required. The lens order.
    :type order: int
    :param parts: Required. The dashboard parts.
    :type parts: dict[str, ~portal.models.DashboardParts]
    :param metadata: The dashboard len's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'order': {'required': True},
        'parts': {'required': True},
    }

    _attribute_map = {
        'order': {'key': 'order', 'type': 'int'},
        'parts': {'key': 'parts', 'type': '{DashboardParts}'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        order: int,
        parts: Dict[str, "DashboardParts"],
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(DashboardLens, self).__init__(**kwargs)
        self.order = order
        self.parts = parts
        self.metadata = metadata


class DashboardListResult(msrest.serialization.Model):
    """List of dashboards.

    :param value: The array of custom resource provider manifests.
    :type value: list[~portal.models.Dashboard]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Dashboard]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Dashboard"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DashboardListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class DashboardParts(msrest.serialization.Model):
    """A dashboard part.

    All required parameters must be populated in order to send to Azure.

    :param position: Required. The dashboard's part position.
    :type position: ~portal.models.DashboardPartsPosition
    :param metadata: The dashboard part's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'position': {'required': True},
    }

    _attribute_map = {
        'position': {'key': 'position', 'type': 'DashboardPartsPosition'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        position: "DashboardPartsPosition",
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(DashboardParts, self).__init__(**kwargs)
        self.position = position
        self.metadata = metadata


class DashboardPartsPosition(msrest.serialization.Model):
    """The dashboard's part position.

    All required parameters must be populated in order to send to Azure.

    :param x: Required. The dashboard's part x coordinate.
    :type x: int
    :param y: Required. The dashboard's part y coordinate.
    :type y: int
    :param row_span: Required. The dashboard's part row span.
    :type row_span: int
    :param col_span: Required. The dashboard's part column span.
    :type col_span: int
    :param metadata: The dashboard part's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'x': {'required': True},
        'y': {'required': True},
        'row_span': {'required': True},
        'col_span': {'required': True},
    }

    _attribute_map = {
        'x': {'key': 'x', 'type': 'int'},
        'y': {'key': 'y', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'},
        'col_span': {'key': 'colSpan', 'type': 'int'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        x: int,
        y: int,
        row_span: int,
        col_span: int,
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(DashboardPartsPosition, self).__init__(**kwargs)
        self.x = x
        self.y = y
        self.row_span = row_span
        self.col_span = col_span
        self.metadata = metadata


class DashboardProperties(msrest.serialization.Model):
    """The shared dashboard properties.

    :param lenses: The dashboard lenses.
    :type lenses: dict[str, ~portal.models.DashboardLens]
    :param metadata: The dashboard metadata.
    :type metadata: dict[str, object]
    """

    _attribute_map = {
        'lenses': {'key': 'lenses', 'type': '{DashboardLens}'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        lenses: Optional[Dict[str, "DashboardLens"]] = None,
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(DashboardProperties, self).__init__(**kwargs)
        self.lenses = lenses
        self.metadata = metadata


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~portal.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponseException(HttpResponseError):
    """Server responded with exception of type: 'ErrorResponse'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorResponseException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'ErrorResponse'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: Error definition.
    :type error: ~portal.models.ErrorDefinition
    """
    _EXCEPTION_TYPE = ErrorResponseException

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinition"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class PatchableDashboard(msrest.serialization.Model):
    """The shared dashboard resource definition.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param lenses: The dashboard lenses.
    :type lenses: dict[str, ~portal.models.DashboardLens]
    :param metadata: The dashboard metadata.
    :type metadata: dict[str, object]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'lenses': {'key': 'properties.lenses', 'type': '{DashboardLens}'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        lenses: Optional[Dict[str, "DashboardLens"]] = None,
        metadata: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(PatchableDashboard, self).__init__(**kwargs)
        self.tags = tags
        self.lenses = lenses
        self.metadata = metadata


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operations of this resource provider.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param is_data_action: Indicates whether the operation applies to data-plane.
    :type is_data_action: str
    :param display: Display metadata associated with the operation.
    :type display: ~portal.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_data_action: Optional[str] = None,
        display: Optional["ResourceProviderOperationDisplay"] = None,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft Custom Providers.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ResourceProviderOperationList(msrest.serialization.Model):
    """Results of the request to list operations.

    :param value: List of operations supported by this resource provider.
    :type value: list[~portal.models.ResourceProviderOperation]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceProviderOperation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
