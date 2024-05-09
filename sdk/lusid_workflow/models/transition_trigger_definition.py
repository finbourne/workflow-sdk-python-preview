# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.992
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


class TransitionTriggerDefinition(object):
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
        'trigger': 'TriggerSchema'
    }

    attribute_map = {
        'name': 'name',
        'trigger': 'trigger'
    }

    required_map = {
        'name': 'required',
        'trigger': 'required'
    }

    def __init__(self, name=None, trigger=None, local_vars_configuration=None):  # noqa: E501
        """TransitionTriggerDefinition - a model defined in OpenAPI"
        
        :param name:  The key/Name of this Trigger (required)
        :type name: str
        :param trigger:  (required)
        :type trigger: lusid_workflow.TriggerSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._trigger = None
        self.discriminator = None

        self.name = name
        self.trigger = trigger

    @property
    def name(self):
        """Gets the name of this TransitionTriggerDefinition.  # noqa: E501

        The key/Name of this Trigger  # noqa: E501

        :return: The name of this TransitionTriggerDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransitionTriggerDefinition.

        The key/Name of this Trigger  # noqa: E501

        :param name: The name of this TransitionTriggerDefinition.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 1024):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._name = name

    @property
    def trigger(self):
        """Gets the trigger of this TransitionTriggerDefinition.  # noqa: E501


        :return: The trigger of this TransitionTriggerDefinition.  # noqa: E501
        :rtype: lusid_workflow.TriggerSchema
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this TransitionTriggerDefinition.


        :param trigger: The trigger of this TransitionTriggerDefinition.  # noqa: E501
        :type trigger: lusid_workflow.TriggerSchema
        """
        if self.local_vars_configuration.client_side_validation and trigger is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger

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
        if not isinstance(other, TransitionTriggerDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitionTriggerDefinition):
            return True

        return self.to_dict() != other.to_dict()
