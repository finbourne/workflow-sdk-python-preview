# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.623
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class TaskDefinitionVersion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'as_at_modified': 'datetime'
    }

    attribute_map = {
        'as_at_modified': 'asAtModified'
    }

    required_map = {
        'as_at_modified': 'optional'
    }

    def __init__(self, as_at_modified=None, local_vars_configuration=None):  # noqa: E501
        """TaskDefinitionVersion - a model defined in OpenAPI"
        
        :param as_at_modified:  The asAt datetime of the Task Definition used by this Task
        :type as_at_modified: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at_modified = None
        self.discriminator = None

        if as_at_modified is not None:
            self.as_at_modified = as_at_modified

    @property
    def as_at_modified(self):
        """Gets the as_at_modified of this TaskDefinitionVersion.  # noqa: E501

        The asAt datetime of the Task Definition used by this Task  # noqa: E501

        :return: The as_at_modified of this TaskDefinitionVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_modified

    @as_at_modified.setter
    def as_at_modified(self, as_at_modified):
        """Sets the as_at_modified of this TaskDefinitionVersion.

        The asAt datetime of the Task Definition used by this Task  # noqa: E501

        :param as_at_modified: The as_at_modified of this TaskDefinitionVersion.  # noqa: E501
        :type as_at_modified: datetime
        """

        self._as_at_modified = as_at_modified

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskDefinitionVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDefinitionVersion):
            return True

        return self.to_dict() != other.to_dict()
