# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1002
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


class TaskTransitionDefinition(object):
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
        'from_state': 'str',
        'to_state': 'str',
        'trigger': 'str',
        'guard': 'str',
        'action': 'str'
    }

    attribute_map = {
        'from_state': 'fromState',
        'to_state': 'toState',
        'trigger': 'trigger',
        'guard': 'guard',
        'action': 'action'
    }

    required_map = {
        'from_state': 'required',
        'to_state': 'required',
        'trigger': 'required',
        'guard': 'optional',
        'action': 'optional'
    }

    def __init__(self, from_state=None, to_state=None, trigger=None, guard=None, action=None, local_vars_configuration=None):  # noqa: E501
        """TaskTransitionDefinition - a model defined in OpenAPI"
        
        :param from_state:  The State this Transition if coming From (required)
        :type from_state: str
        :param to_state:  The State this Transition is going To (required)
        :type to_state: str
        :param trigger:  The Trigger for this Transition (required)
        :type trigger: str
        :param guard:  The Guard for this Transition, if any
        :type guard: str
        :param action:  The Action to invoke on successful Transition
        :type action: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_state = None
        self._to_state = None
        self._trigger = None
        self._guard = None
        self._action = None
        self.discriminator = None

        self.from_state = from_state
        self.to_state = to_state
        self.trigger = trigger
        self.guard = guard
        self.action = action

    @property
    def from_state(self):
        """Gets the from_state of this TaskTransitionDefinition.  # noqa: E501

        The State this Transition if coming From  # noqa: E501

        :return: The from_state of this TaskTransitionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._from_state

    @from_state.setter
    def from_state(self, from_state):
        """Sets the from_state of this TaskTransitionDefinition.

        The State this Transition if coming From  # noqa: E501

        :param from_state: The from_state of this TaskTransitionDefinition.  # noqa: E501
        :type from_state: str
        """
        if self.local_vars_configuration.client_side_validation and from_state is None:  # noqa: E501
            raise ValueError("Invalid value for `from_state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                from_state is not None and len(from_state) > 1024):
            raise ValueError("Invalid value for `from_state`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                from_state is not None and len(from_state) < 1):
            raise ValueError("Invalid value for `from_state`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                from_state is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', from_state)):  # noqa: E501
            raise ValueError(r"Invalid value for `from_state`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._from_state = from_state

    @property
    def to_state(self):
        """Gets the to_state of this TaskTransitionDefinition.  # noqa: E501

        The State this Transition is going To  # noqa: E501

        :return: The to_state of this TaskTransitionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._to_state

    @to_state.setter
    def to_state(self, to_state):
        """Sets the to_state of this TaskTransitionDefinition.

        The State this Transition is going To  # noqa: E501

        :param to_state: The to_state of this TaskTransitionDefinition.  # noqa: E501
        :type to_state: str
        """
        if self.local_vars_configuration.client_side_validation and to_state is None:  # noqa: E501
            raise ValueError("Invalid value for `to_state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_state is not None and len(to_state) > 1024):
            raise ValueError("Invalid value for `to_state`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_state is not None and len(to_state) < 1):
            raise ValueError("Invalid value for `to_state`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_state is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', to_state)):  # noqa: E501
            raise ValueError(r"Invalid value for `to_state`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._to_state = to_state

    @property
    def trigger(self):
        """Gets the trigger of this TaskTransitionDefinition.  # noqa: E501

        The Trigger for this Transition  # noqa: E501

        :return: The trigger of this TaskTransitionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this TaskTransitionDefinition.

        The Trigger for this Transition  # noqa: E501

        :param trigger: The trigger of this TaskTransitionDefinition.  # noqa: E501
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

    @property
    def guard(self):
        """Gets the guard of this TaskTransitionDefinition.  # noqa: E501

        The Guard for this Transition, if any  # noqa: E501

        :return: The guard of this TaskTransitionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._guard

    @guard.setter
    def guard(self, guard):
        """Sets the guard of this TaskTransitionDefinition.

        The Guard for this Transition, if any  # noqa: E501

        :param guard: The guard of this TaskTransitionDefinition.  # noqa: E501
        :type guard: str
        """
        if (self.local_vars_configuration.client_side_validation and
                guard is not None and len(guard) > 1024):
            raise ValueError("Invalid value for `guard`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                guard is not None and len(guard) < 1):
            raise ValueError("Invalid value for `guard`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                guard is not None and not re.search(r'^[\s\S]*$', guard)):  # noqa: E501
            raise ValueError(r"Invalid value for `guard`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._guard = guard

    @property
    def action(self):
        """Gets the action of this TaskTransitionDefinition.  # noqa: E501

        The Action to invoke on successful Transition  # noqa: E501

        :return: The action of this TaskTransitionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TaskTransitionDefinition.

        The Action to invoke on successful Transition  # noqa: E501

        :param action: The action of this TaskTransitionDefinition.  # noqa: E501
        :type action: str
        """
        if (self.local_vars_configuration.client_side_validation and
                action is not None and len(action) > 1024):
            raise ValueError("Invalid value for `action`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                action is not None and len(action) < 1):
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                action is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', action)):  # noqa: E501
            raise ValueError(r"Invalid value for `action`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._action = action

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
        if not isinstance(other, TaskTransitionDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskTransitionDefinition):
            return True

        return self.to_dict() != other.to_dict()
