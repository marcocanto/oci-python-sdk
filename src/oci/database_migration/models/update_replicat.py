# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateReplicat(object):
    """
    Parameters for Replicat processes.
    If an empty object is specified, the stored Replicat details will be removed.
    """

    #: A constant which can be used with the performance_profile property of a UpdateReplicat.
    #: This constant has a value of "LOW"
    PERFORMANCE_PROFILE_LOW = "LOW"

    #: A constant which can be used with the performance_profile property of a UpdateReplicat.
    #: This constant has a value of "HIGH"
    PERFORMANCE_PROFILE_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateReplicat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param performance_profile:
            The value to assign to the performance_profile property of this UpdateReplicat.
            Allowed values for this property are: "LOW", "HIGH"
        :type performance_profile: str

        :param map_parallelism:
            The value to assign to the map_parallelism property of this UpdateReplicat.
        :type map_parallelism: int

        :param min_apply_parallelism:
            The value to assign to the min_apply_parallelism property of this UpdateReplicat.
        :type min_apply_parallelism: int

        :param max_apply_parallelism:
            The value to assign to the max_apply_parallelism property of this UpdateReplicat.
        :type max_apply_parallelism: int

        """
        self.swagger_types = {
            'performance_profile': 'str',
            'map_parallelism': 'int',
            'min_apply_parallelism': 'int',
            'max_apply_parallelism': 'int'
        }

        self.attribute_map = {
            'performance_profile': 'performanceProfile',
            'map_parallelism': 'mapParallelism',
            'min_apply_parallelism': 'minApplyParallelism',
            'max_apply_parallelism': 'maxApplyParallelism'
        }

        self._performance_profile = None
        self._map_parallelism = None
        self._min_apply_parallelism = None
        self._max_apply_parallelism = None

    @property
    def performance_profile(self):
        """
        Gets the performance_profile of this UpdateReplicat.
        Replicat performance.

        Allowed values for this property are: "LOW", "HIGH"


        :return: The performance_profile of this UpdateReplicat.
        :rtype: str
        """
        return self._performance_profile

    @performance_profile.setter
    def performance_profile(self, performance_profile):
        """
        Sets the performance_profile of this UpdateReplicat.
        Replicat performance.


        :param performance_profile: The performance_profile of this UpdateReplicat.
        :type: str
        """
        allowed_values = ["LOW", "HIGH"]
        if not value_allowed_none_or_none_sentinel(performance_profile, allowed_values):
            raise ValueError(
                "Invalid value for `performance_profile`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._performance_profile = performance_profile

    @property
    def map_parallelism(self):
        """
        Gets the map_parallelism of this UpdateReplicat.
        Number of threads used to read trail files (valid for Parallel Replicat)


        :return: The map_parallelism of this UpdateReplicat.
        :rtype: int
        """
        return self._map_parallelism

    @map_parallelism.setter
    def map_parallelism(self, map_parallelism):
        """
        Sets the map_parallelism of this UpdateReplicat.
        Number of threads used to read trail files (valid for Parallel Replicat)


        :param map_parallelism: The map_parallelism of this UpdateReplicat.
        :type: int
        """
        self._map_parallelism = map_parallelism

    @property
    def min_apply_parallelism(self):
        """
        Gets the min_apply_parallelism of this UpdateReplicat.
        Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :return: The min_apply_parallelism of this UpdateReplicat.
        :rtype: int
        """
        return self._min_apply_parallelism

    @min_apply_parallelism.setter
    def min_apply_parallelism(self, min_apply_parallelism):
        """
        Sets the min_apply_parallelism of this UpdateReplicat.
        Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :param min_apply_parallelism: The min_apply_parallelism of this UpdateReplicat.
        :type: int
        """
        self._min_apply_parallelism = min_apply_parallelism

    @property
    def max_apply_parallelism(self):
        """
        Gets the max_apply_parallelism of this UpdateReplicat.
        Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :return: The max_apply_parallelism of this UpdateReplicat.
        :rtype: int
        """
        return self._max_apply_parallelism

    @max_apply_parallelism.setter
    def max_apply_parallelism(self, max_apply_parallelism):
        """
        Sets the max_apply_parallelism of this UpdateReplicat.
        Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :param max_apply_parallelism: The max_apply_parallelism of this UpdateReplicat.
        :type: int
        """
        self._max_apply_parallelism = max_apply_parallelism

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
