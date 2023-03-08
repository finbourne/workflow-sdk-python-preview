# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.157
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


class Trigger(object):
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
        'name': 'str',
        'schema': 'TriggerSchema'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema'
    }

    required_map = {
        'name': 'optional',
        'schema': 'optional'
    }

    def __init__(self, name=None, schema=None, local_vars_configuration=None):  # noqa: E501
        """Trigger - a model defined in OpenAPI"
        
        :param name:  The key/Name of this Trigger
        :type name: str
        :param schema: 
        :type schema: lusid_workflow.TriggerSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._schema = None
        self.discriminator = None

        self.name = name
        if schema is not None:
            self.schema = schema

    @property
    def name(self):
        """Gets the name of this Trigger.  # noqa: E501

        The key/Name of this Trigger  # noqa: E501

        :return: The name of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Trigger.

        The key/Name of this Trigger  # noqa: E501

        :param name: The name of this Trigger.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this Trigger.  # noqa: E501


        :return: The schema of this Trigger.  # noqa: E501
        :rtype: lusid_workflow.TriggerSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Trigger.


        :param schema: The schema of this Trigger.  # noqa: E501
        :type schema: lusid_workflow.TriggerSchema
        """

        self._schema = schema

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
        if not isinstance(other, Trigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trigger):
            return True

        return self.to_dict() != other.to_dict()
