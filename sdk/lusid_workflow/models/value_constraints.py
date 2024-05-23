# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1050
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


class ValueConstraints(object):
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
        'constraint_type': 'str',
        'value_source_type': 'str',
        'acceptable_values': 'list[object]'
    }

    attribute_map = {
        'constraint_type': 'constraintType',
        'value_source_type': 'valueSourceType',
        'acceptable_values': 'acceptableValues'
    }

    required_map = {
        'constraint_type': 'required',
        'value_source_type': 'required',
        'acceptable_values': 'required'
    }

    def __init__(self, constraint_type=None, value_source_type=None, acceptable_values=None, local_vars_configuration=None):  # noqa: E501
        """ValueConstraints - a model defined in OpenAPI"
        
        :param constraint_type:  Whether the constraint is a suggestion or should be enforced via validation (required)
        :type constraint_type: str
        :param value_source_type:  The source of the acceptable values (required)
        :type value_source_type: str
        :param acceptable_values:  The acceptable values for the field (required)
        :type acceptable_values: list[object]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._constraint_type = None
        self._value_source_type = None
        self._acceptable_values = None
        self.discriminator = None

        self.constraint_type = constraint_type
        self.value_source_type = value_source_type
        self.acceptable_values = acceptable_values

    @property
    def constraint_type(self):
        """Gets the constraint_type of this ValueConstraints.  # noqa: E501

        Whether the constraint is a suggestion or should be enforced via validation  # noqa: E501

        :return: The constraint_type of this ValueConstraints.  # noqa: E501
        :rtype: str
        """
        return self._constraint_type

    @constraint_type.setter
    def constraint_type(self, constraint_type):
        """Sets the constraint_type of this ValueConstraints.

        Whether the constraint is a suggestion or should be enforced via validation  # noqa: E501

        :param constraint_type: The constraint_type of this ValueConstraints.  # noqa: E501
        :type constraint_type: str
        """
        if self.local_vars_configuration.client_side_validation and constraint_type is None:  # noqa: E501
            raise ValueError("Invalid value for `constraint_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                constraint_type is not None and len(constraint_type) < 1):
            raise ValueError("Invalid value for `constraint_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._constraint_type = constraint_type

    @property
    def value_source_type(self):
        """Gets the value_source_type of this ValueConstraints.  # noqa: E501

        The source of the acceptable values  # noqa: E501

        :return: The value_source_type of this ValueConstraints.  # noqa: E501
        :rtype: str
        """
        return self._value_source_type

    @value_source_type.setter
    def value_source_type(self, value_source_type):
        """Sets the value_source_type of this ValueConstraints.

        The source of the acceptable values  # noqa: E501

        :param value_source_type: The value_source_type of this ValueConstraints.  # noqa: E501
        :type value_source_type: str
        """
        if self.local_vars_configuration.client_side_validation and value_source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_source_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value_source_type is not None and len(value_source_type) < 1):
            raise ValueError("Invalid value for `value_source_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._value_source_type = value_source_type

    @property
    def acceptable_values(self):
        """Gets the acceptable_values of this ValueConstraints.  # noqa: E501

        The acceptable values for the field  # noqa: E501

        :return: The acceptable_values of this ValueConstraints.  # noqa: E501
        :rtype: list[object]
        """
        return self._acceptable_values

    @acceptable_values.setter
    def acceptable_values(self, acceptable_values):
        """Sets the acceptable_values of this ValueConstraints.

        The acceptable values for the field  # noqa: E501

        :param acceptable_values: The acceptable_values of this ValueConstraints.  # noqa: E501
        :type acceptable_values: list[object]
        """
        if self.local_vars_configuration.client_side_validation and acceptable_values is None:  # noqa: E501
            raise ValueError("Invalid value for `acceptable_values`, must not be `None`")  # noqa: E501

        self._acceptable_values = acceptable_values

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
        if not isinstance(other, ValueConstraints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueConstraints):
            return True

        return self.to_dict() != other.to_dict()
