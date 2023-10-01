# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AgentConfiguration
    from ._models_py3 import AgentUpgrade
    from ._models_py3 import AgentVersion
    from ._models_py3 import AgentVersionsList
    from ._models_py3 import AvailablePatchCountByClassification
    from ._models_py3 import CloudMetadata
    from ._models_py3 import ConfigurationExtension
    from ._models_py3 import ConnectionDetail
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorDetailAutoGenerated
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseAutoGenerated
    from ._models_py3 import ExtensionTargetProperties
    from ._models_py3 import ExtensionValue
    from ._models_py3 import ExtensionValueListResult
    from ._models_py3 import HybridComputePrivateLinkScope
    from ._models_py3 import HybridComputePrivateLinkScopeListResult
    from ._models_py3 import HybridComputePrivateLinkScopeProperties
    from ._models_py3 import HybridIdentityMetadata
    from ._models_py3 import HybridIdentityMetadataList
    from ._models_py3 import Identity
    from ._models_py3 import IpAddress
    from ._models_py3 import LinuxParameters
    from ._models_py3 import LocationData
    from ._models_py3 import Machine
    from ._models_py3 import MachineAssessPatchesResult
    from ._models_py3 import MachineExtension
    from ._models_py3 import MachineExtensionInstanceView
    from ._models_py3 import MachineExtensionInstanceViewStatus
    from ._models_py3 import MachineExtensionUpdate
    from ._models_py3 import MachineExtensionUpgrade
    from ._models_py3 import MachineExtensionsListResult
    from ._models_py3 import MachineInstallPatchesParameters
    from ._models_py3 import MachineInstallPatchesResult
    from ._models_py3 import MachineListResult
    from ._models_py3 import MachineRunCommand
    from ._models_py3 import MachineRunCommandInstanceView
    from ._models_py3 import MachineRunCommandInstanceViewStatus
    from ._models_py3 import MachineRunCommandScriptSource
    from ._models_py3 import MachineRunCommandUpdate
    from ._models_py3 import MachineRunCommandsListResult
    from ._models_py3 import MachineUpdate
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OSProfile
    from ._models_py3 import OSProfileLinuxConfiguration
    from ._models_py3 import OSProfileWindowsConfiguration
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationValue
    from ._models_py3 import OperationValueDisplay
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionDataModel
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointConnectionProperties
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkScopeValidationDetails
    from ._models_py3 import PrivateLinkScopesResource
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourceUpdate
    from ._models_py3 import RunCommandInputParameter
    from ._models_py3 import RunCommandManagedIdentity
    from ._models_py3 import ServiceStatus
    from ._models_py3 import ServiceStatuses
    from ._models_py3 import Subnet
    from ._models_py3 import SystemData
    from ._models_py3 import TagsResource
    from ._models_py3 import TrackedResource
    from ._models_py3 import WindowsParameters
except (SyntaxError, ImportError):
    from ._models import AgentConfiguration  # type: ignore
    from ._models import AgentUpgrade  # type: ignore
    from ._models import AgentVersion  # type: ignore
    from ._models import AgentVersionsList  # type: ignore
    from ._models import AvailablePatchCountByClassification  # type: ignore
    from ._models import CloudMetadata  # type: ignore
    from ._models import ConfigurationExtension  # type: ignore
    from ._models import ConnectionDetail  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorDetailAutoGenerated  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseAutoGenerated  # type: ignore
    from ._models import ExtensionTargetProperties  # type: ignore
    from ._models import ExtensionValue  # type: ignore
    from ._models import ExtensionValueListResult  # type: ignore
    from ._models import HybridComputePrivateLinkScope  # type: ignore
    from ._models import HybridComputePrivateLinkScopeListResult  # type: ignore
    from ._models import HybridComputePrivateLinkScopeProperties  # type: ignore
    from ._models import HybridIdentityMetadata  # type: ignore
    from ._models import HybridIdentityMetadataList  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import IpAddress  # type: ignore
    from ._models import LinuxParameters  # type: ignore
    from ._models import LocationData  # type: ignore
    from ._models import Machine  # type: ignore
    from ._models import MachineAssessPatchesResult  # type: ignore
    from ._models import MachineExtension  # type: ignore
    from ._models import MachineExtensionInstanceView  # type: ignore
    from ._models import MachineExtensionInstanceViewStatus  # type: ignore
    from ._models import MachineExtensionUpdate  # type: ignore
    from ._models import MachineExtensionUpgrade  # type: ignore
    from ._models import MachineExtensionsListResult  # type: ignore
    from ._models import MachineInstallPatchesParameters  # type: ignore
    from ._models import MachineInstallPatchesResult  # type: ignore
    from ._models import MachineListResult  # type: ignore
    from ._models import MachineRunCommand  # type: ignore
    from ._models import MachineRunCommandInstanceView  # type: ignore
    from ._models import MachineRunCommandInstanceViewStatus  # type: ignore
    from ._models import MachineRunCommandScriptSource  # type: ignore
    from ._models import MachineRunCommandUpdate  # type: ignore
    from ._models import MachineRunCommandsListResult  # type: ignore
    from ._models import MachineUpdate  # type: ignore
    from ._models import NetworkInterface  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import OSProfile  # type: ignore
    from ._models import OSProfileLinuxConfiguration  # type: ignore
    from ._models import OSProfileWindowsConfiguration  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationValue  # type: ignore
    from ._models import OperationValueDisplay  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionDataModel  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointConnectionProperties  # type: ignore
    from ._models import PrivateEndpointProperty  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkResourceProperties  # type: ignore
    from ._models import PrivateLinkScopeValidationDetails  # type: ignore
    from ._models import PrivateLinkScopesResource  # type: ignore
    from ._models import PrivateLinkServiceConnectionStateProperty  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceUpdate  # type: ignore
    from ._models import RunCommandInputParameter  # type: ignore
    from ._models import RunCommandManagedIdentity  # type: ignore
    from ._models import ServiceStatus  # type: ignore
    from ._models import ServiceStatuses  # type: ignore
    from ._models import Subnet  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TagsResource  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import WindowsParameters  # type: ignore

from ._hybrid_compute_management_client_enums import (
    AgentConfigurationMode,
    AssessmentModeTypes,
    CreatedByType,
    InstanceViewTypes,
    LastAttemptStatusEnum,
    OsType,
    PatchModeTypes,
    PatchOperationStartedBy,
    PatchOperationStatus,
    PatchServiceUsed,
    PrivateCloudKind,
    PublicNetworkAccessType,
    StatusLevelTypes,
    StatusTypes,
    VMGuestPatchClassificationLinux,
    VMGuestPatchClassificationWindows,
    VMGuestPatchRebootSetting,
    VMGuestPatchRebootStatus,
)

__all__ = [
    'AgentConfiguration',
    'AgentUpgrade',
    'AgentVersion',
    'AgentVersionsList',
    'AvailablePatchCountByClassification',
    'CloudMetadata',
    'ConfigurationExtension',
    'ConnectionDetail',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorDetailAutoGenerated',
    'ErrorResponse',
    'ErrorResponseAutoGenerated',
    'ExtensionTargetProperties',
    'ExtensionValue',
    'ExtensionValueListResult',
    'HybridComputePrivateLinkScope',
    'HybridComputePrivateLinkScopeListResult',
    'HybridComputePrivateLinkScopeProperties',
    'HybridIdentityMetadata',
    'HybridIdentityMetadataList',
    'Identity',
    'IpAddress',
    'LinuxParameters',
    'LocationData',
    'Machine',
    'MachineAssessPatchesResult',
    'MachineExtension',
    'MachineExtensionInstanceView',
    'MachineExtensionInstanceViewStatus',
    'MachineExtensionUpdate',
    'MachineExtensionUpgrade',
    'MachineExtensionsListResult',
    'MachineInstallPatchesParameters',
    'MachineInstallPatchesResult',
    'MachineListResult',
    'MachineRunCommand',
    'MachineRunCommandInstanceView',
    'MachineRunCommandInstanceViewStatus',
    'MachineRunCommandScriptSource',
    'MachineRunCommandUpdate',
    'MachineRunCommandsListResult',
    'MachineUpdate',
    'NetworkInterface',
    'NetworkProfile',
    'OSProfile',
    'OSProfileLinuxConfiguration',
    'OSProfileWindowsConfiguration',
    'OperationListResult',
    'OperationValue',
    'OperationValueDisplay',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionDataModel',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointConnectionProperties',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkScopeValidationDetails',
    'PrivateLinkScopesResource',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'Resource',
    'ResourceUpdate',
    'RunCommandInputParameter',
    'RunCommandManagedIdentity',
    'ServiceStatus',
    'ServiceStatuses',
    'Subnet',
    'SystemData',
    'TagsResource',
    'TrackedResource',
    'WindowsParameters',
    'AgentConfigurationMode',
    'AssessmentModeTypes',
    'CreatedByType',
    'InstanceViewTypes',
    'LastAttemptStatusEnum',
    'OsType',
    'PatchModeTypes',
    'PatchOperationStartedBy',
    'PatchOperationStatus',
    'PatchServiceUsed',
    'PrivateCloudKind',
    'PublicNetworkAccessType',
    'StatusLevelTypes',
    'StatusTypes',
    'VMGuestPatchClassificationLinux',
    'VMGuestPatchClassificationWindows',
    'VMGuestPatchRebootSetting',
    'VMGuestPatchRebootStatus',
]