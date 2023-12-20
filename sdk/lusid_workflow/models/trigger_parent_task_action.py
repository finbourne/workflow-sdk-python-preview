# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.680
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


class TriggerParentTaskAction(object):
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
        'type': 'str',
        'trigger': 'str'
    }

    attribute_map = {
        'type': 'type',
        'trigger': 'trigger'
    }

    required_map = {
        'type': 'required',
        'trigger': 'required'
    }

    def __init__(self, type=None, trigger=None, local_vars_configuration=None):  # noqa: E501
        """TriggerParentTaskAction - a model defined in OpenAPI"
        
        :param type:  Type name for this Action (required)
        :type type: str
        :param trigger:  Trigger on parent task to be invoked (required)
        :type trigger: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._trigger = None
        self.discriminator = None

        self.type = type
        self.trigger = trigger

    @property
    def type(self):
        """Gets the type of this TriggerParentTaskAction.  # noqa: E501

        Type name for this Action  # noqa: E501

        :return: The type of this TriggerParentTaskAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TriggerParentTaskAction.

        Type name for this Action  # noqa: E501

        :param type: The type of this TriggerParentTaskAction.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["TriggerParentTask"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def trigger(self):
        """Gets the trigger of this TriggerParentTaskAction.  # noqa: E501

        Trigger on parent task to be invoked  # noqa: E501

        :return: The trigger of this TriggerParentTaskAction.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this TriggerParentTaskAction.

        Trigger on parent task to be invoked  # noqa: E501

        :param trigger: The trigger of this TriggerParentTaskAction.  # noqa: E501
        :type trigger: str
        """
        if self.local_vars_configuration.client_side_validation and trigger is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger is not None and len(trigger) > 1024):
            raise ValueError("Invalid value for `trigger`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger is not None and len(trigger) < 1):
            raise ValueError("Invalid value for `trigger`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', trigger)):  # noqa: E501
            raise ValueError(r"Invalid value for `trigger`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

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
        if not isinstance(other, TriggerParentTaskAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TriggerParentTaskAction):
            return True

        return self.to_dict() != other.to_dict()
