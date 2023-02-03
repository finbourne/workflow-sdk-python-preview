# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.128
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


class UpdateTaskRequest(object):
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
        'field': 'str',
        'value': 'str'
    }

    attribute_map = {
        'field': 'field',
        'value': 'value'
    }

    required_map = {
        'field': 'optional',
        'value': 'optional'
    }

    def __init__(self, field=None, value=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTaskRequest - a model defined in OpenAPI"
        
        :param field:  The Field this Update is reporting; this is synonymous with FieldSchema.Name
        :type field: str
        :param value:  String representation of the data itself
        :type value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._value = None
        self.discriminator = None

        self.field = field
        self.value = value

    @property
    def field(self):
        """Gets the field of this UpdateTaskRequest.  # noqa: E501

        The Field this Update is reporting; this is synonymous with FieldSchema.Name  # noqa: E501

        :return: The field of this UpdateTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this UpdateTaskRequest.

        The Field this Update is reporting; this is synonymous with FieldSchema.Name  # noqa: E501

        :param field: The field of this UpdateTaskRequest.  # noqa: E501
        :type field: str
        """

        self._field = field

    @property
    def value(self):
        """Gets the value of this UpdateTaskRequest.  # noqa: E501

        String representation of the data itself  # noqa: E501

        :return: The value of this UpdateTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateTaskRequest.

        String representation of the data itself  # noqa: E501

        :param value: The value of this UpdateTaskRequest.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, UpdateTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
