# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousVirtualMachine(object):
    """
    Autonomous Virtual Machine details.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVirtualMachine.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousVirtualMachine object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousVirtualMachine.
        :type id: str

        :param vm_name:
            The value to assign to the vm_name property of this AutonomousVirtualMachine.
        :type vm_name: str

        :param db_server_id:
            The value to assign to the db_server_id property of this AutonomousVirtualMachine.
        :type db_server_id: str

        :param db_server_display_name:
            The value to assign to the db_server_display_name property of this AutonomousVirtualMachine.
        :type db_server_display_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this AutonomousVirtualMachine.
        :type cpu_core_count: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this AutonomousVirtualMachine.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this AutonomousVirtualMachine.
        :type db_node_storage_size_in_gbs: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousVirtualMachine.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param client_ip_address:
            The value to assign to the client_ip_address property of this AutonomousVirtualMachine.
        :type client_ip_address: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousVirtualMachine.
        :type compartment_id: str

        :param autonomous_vm_cluster_id:
            The value to assign to the autonomous_vm_cluster_id property of this AutonomousVirtualMachine.
        :type autonomous_vm_cluster_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousVirtualMachine.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousVirtualMachine.
        :type defined_tags: dict(str, dict(str, object))

        :param cloud_autonomous_vm_cluster_id:
            The value to assign to the cloud_autonomous_vm_cluster_id property of this AutonomousVirtualMachine.
        :type cloud_autonomous_vm_cluster_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'vm_name': 'str',
            'db_server_id': 'str',
            'db_server_display_name': 'str',
            'cpu_core_count': 'int',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'lifecycle_state': 'str',
            'client_ip_address': 'str',
            'compartment_id': 'str',
            'autonomous_vm_cluster_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'cloud_autonomous_vm_cluster_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'vm_name': 'vmName',
            'db_server_id': 'dbServerId',
            'db_server_display_name': 'dbServerDisplayName',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'lifecycle_state': 'lifecycleState',
            'client_ip_address': 'clientIpAddress',
            'compartment_id': 'compartmentId',
            'autonomous_vm_cluster_id': 'autonomousVmClusterId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'cloud_autonomous_vm_cluster_id': 'cloudAutonomousVmClusterId'
        }

        self._id = None
        self._vm_name = None
        self._db_server_id = None
        self._db_server_display_name = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._lifecycle_state = None
        self._client_ip_address = None
        self._compartment_id = None
        self._autonomous_vm_cluster_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._cloud_autonomous_vm_cluster_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousVirtualMachine.
        The `OCID`__ of the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousVirtualMachine.
        The `OCID`__ of the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousVirtualMachine.
        :type: str
        """
        self._id = id

    @property
    def vm_name(self):
        """
        Gets the vm_name of this AutonomousVirtualMachine.
        The name of the Autonomous Virtual Machine.


        :return: The vm_name of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """
        Sets the vm_name of this AutonomousVirtualMachine.
        The name of the Autonomous Virtual Machine.


        :param vm_name: The vm_name of this AutonomousVirtualMachine.
        :type: str
        """
        self._vm_name = vm_name

    @property
    def db_server_id(self):
        """
        Gets the db_server_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Db server associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_server_id of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._db_server_id

    @db_server_id.setter
    def db_server_id(self, db_server_id):
        """
        Sets the db_server_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Db server associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_server_id: The db_server_id of this AutonomousVirtualMachine.
        :type: str
        """
        self._db_server_id = db_server_id

    @property
    def db_server_display_name(self):
        """
        Gets the db_server_display_name of this AutonomousVirtualMachine.
        The display name of the dbServer associated with the Autonomous Virtual Machine.


        :return: The db_server_display_name of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._db_server_display_name

    @db_server_display_name.setter
    def db_server_display_name(self, db_server_display_name):
        """
        Sets the db_server_display_name of this AutonomousVirtualMachine.
        The display name of the dbServer associated with the Autonomous Virtual Machine.


        :param db_server_display_name: The db_server_display_name of this AutonomousVirtualMachine.
        :type: str
        """
        self._db_server_display_name = db_server_display_name

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this AutonomousVirtualMachine.
        The number of CPU cores enabled on the Autonomous Virtual Machine.


        :return: The cpu_core_count of this AutonomousVirtualMachine.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this AutonomousVirtualMachine.
        The number of CPU cores enabled on the Autonomous Virtual Machine.


        :param cpu_core_count: The cpu_core_count of this AutonomousVirtualMachine.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this AutonomousVirtualMachine.
        The allocated memory in GBs on the Autonomous Virtual Machine.


        :return: The memory_size_in_gbs of this AutonomousVirtualMachine.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this AutonomousVirtualMachine.
        The allocated memory in GBs on the Autonomous Virtual Machine.


        :param memory_size_in_gbs: The memory_size_in_gbs of this AutonomousVirtualMachine.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this AutonomousVirtualMachine.
        The allocated local node storage in GBs on the Autonomous Virtual Machine.


        :return: The db_node_storage_size_in_gbs of this AutonomousVirtualMachine.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this AutonomousVirtualMachine.
        The allocated local node storage in GBs on the Autonomous Virtual Machine.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this AutonomousVirtualMachine.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousVirtualMachine.
        The current state of the Autonomous Virtual Machine.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousVirtualMachine.
        The current state of the Autonomous Virtual Machine.


        :param lifecycle_state: The lifecycle_state of this AutonomousVirtualMachine.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def client_ip_address(self):
        """
        Gets the client_ip_address of this AutonomousVirtualMachine.
        Client IP Address.


        :return: The client_ip_address of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """
        Sets the client_ip_address of this AutonomousVirtualMachine.
        Client IP Address.


        :param client_ip_address: The client_ip_address of this AutonomousVirtualMachine.
        :type: str
        """
        self._client_ip_address = client_ip_address

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AutonomousVirtualMachine.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousVirtualMachine.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousVirtualMachine.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def autonomous_vm_cluster_id(self):
        """
        Gets the autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Autonomous VM Cluster associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._autonomous_vm_cluster_id

    @autonomous_vm_cluster_id.setter
    def autonomous_vm_cluster_id(self, autonomous_vm_cluster_id):
        """
        Sets the autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Autonomous VM Cluster associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_vm_cluster_id: The autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        :type: str
        """
        self._autonomous_vm_cluster_id = autonomous_vm_cluster_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousVirtualMachine.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousVirtualMachine.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousVirtualMachine.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousVirtualMachine.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousVirtualMachine.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousVirtualMachine.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousVirtualMachine.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousVirtualMachine.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def cloud_autonomous_vm_cluster_id(self):
        """
        Gets the cloud_autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Cloud Autonomous VM Cluster associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        :rtype: str
        """
        return self._cloud_autonomous_vm_cluster_id

    @cloud_autonomous_vm_cluster_id.setter
    def cloud_autonomous_vm_cluster_id(self, cloud_autonomous_vm_cluster_id):
        """
        Sets the cloud_autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        The `OCID`__ of the Cloud Autonomous VM Cluster associated with the Autonomous Virtual Machine.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_autonomous_vm_cluster_id: The cloud_autonomous_vm_cluster_id of this AutonomousVirtualMachine.
        :type: str
        """
        self._cloud_autonomous_vm_cluster_id = cloud_autonomous_vm_cluster_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
