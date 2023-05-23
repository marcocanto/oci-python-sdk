# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousVmClusterResourceDetails(object):
    """
    Unallocated resource details of the AVM
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousVmClusterResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousVmClusterResourceDetails.
        :type id: str

        :param un_allocated_adb_storage_in_tbs:
            The value to assign to the un_allocated_adb_storage_in_tbs property of this AutonomousVmClusterResourceDetails.
        :type un_allocated_adb_storage_in_tbs: float

        """
        self.swagger_types = {
            'id': 'str',
            'un_allocated_adb_storage_in_tbs': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'un_allocated_adb_storage_in_tbs': 'unAllocatedAdbStorageInTBs'
        }

        self._id = None
        self._un_allocated_adb_storage_in_tbs = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousVmClusterResourceDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousVmClusterResourceDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousVmClusterResourceDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousVmClusterResourceDetails.
        :type: str
        """
        self._id = id

    @property
    def un_allocated_adb_storage_in_tbs(self):
        """
        **[Required]** Gets the un_allocated_adb_storage_in_tbs of this AutonomousVmClusterResourceDetails.
        Total unallocated autonomous data storage in the AVM in TBs.


        :return: The un_allocated_adb_storage_in_tbs of this AutonomousVmClusterResourceDetails.
        :rtype: float
        """
        return self._un_allocated_adb_storage_in_tbs

    @un_allocated_adb_storage_in_tbs.setter
    def un_allocated_adb_storage_in_tbs(self, un_allocated_adb_storage_in_tbs):
        """
        Sets the un_allocated_adb_storage_in_tbs of this AutonomousVmClusterResourceDetails.
        Total unallocated autonomous data storage in the AVM in TBs.


        :param un_allocated_adb_storage_in_tbs: The un_allocated_adb_storage_in_tbs of this AutonomousVmClusterResourceDetails.
        :type: float
        """
        self._un_allocated_adb_storage_in_tbs = un_allocated_adb_storage_in_tbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
