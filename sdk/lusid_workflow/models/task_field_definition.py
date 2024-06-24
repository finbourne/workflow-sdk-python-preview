# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1141
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


class TaskFieldDefinition(object):
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
        'type': 'str',
        'read_only_states': 'ReadOnlyStates',
        'value_constraints': 'ValueConstraints'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'read_only_states': 'readOnlyStates',
        'value_constraints': 'valueConstraints'
    }

    required_map = {
        'name': 'required',
        'type': 'required',
        'read_only_states': 'optional',
        'value_constraints': 'optional'
    }

    def __init__(self, name=None, type=None, read_only_states=None, value_constraints=None, local_vars_configuration=None):  # noqa: E501
        """TaskFieldDefinition - a model defined in OpenAPI"
        
        :param name:  The name of this Field (required)
        :type name: str
        :param type:  The value type for the field. Available values are: \"String\", \"Decimal\", \"DateTime\", \"Boolean\") (required)
        :type type: str
        :param read_only_states: 
        :type read_only_states: lusid_workflow.ReadOnlyStates
        :param value_constraints: 
        :type value_constraints: lusid_workflow.ValueConstraints

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._read_only_states = None
        self._value_constraints = None
        self.discriminator = None

        self.name = name
        self.type = type
        if read_only_states is not None:
            self.read_only_states = read_only_states
        if value_constraints is not None:
            self.value_constraints = value_constraints

    @property
    def name(self):
        """Gets the name of this TaskFieldDefinition.  # noqa: E501

        The name of this Field  # noqa: E501

        :return: The name of this TaskFieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskFieldDefinition.

        The name of this Field  # noqa: E501

        :param name: The name of this TaskFieldDefinition.  # noqa: E501
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
    def type(self):
        """Gets the type of this TaskFieldDefinition.  # noqa: E501

        The value type for the field. Available values are: \"String\", \"Decimal\", \"DateTime\", \"Boolean\")  # noqa: E501

        :return: The type of this TaskFieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskFieldDefinition.

        The value type for the field. Available values are: \"String\", \"Decimal\", \"DateTime\", \"Boolean\")  # noqa: E501

        :param type: The type of this TaskFieldDefinition.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def read_only_states(self):
        """Gets the read_only_states of this TaskFieldDefinition.  # noqa: E501


        :return: The read_only_states of this TaskFieldDefinition.  # noqa: E501
        :rtype: lusid_workflow.ReadOnlyStates
        """
        return self._read_only_states

    @read_only_states.setter
    def read_only_states(self, read_only_states):
        """Sets the read_only_states of this TaskFieldDefinition.


        :param read_only_states: The read_only_states of this TaskFieldDefinition.  # noqa: E501
        :type read_only_states: lusid_workflow.ReadOnlyStates
        """

        self._read_only_states = read_only_states

    @property
    def value_constraints(self):
        """Gets the value_constraints of this TaskFieldDefinition.  # noqa: E501


        :return: The value_constraints of this TaskFieldDefinition.  # noqa: E501
        :rtype: lusid_workflow.ValueConstraints
        """
        return self._value_constraints

    @value_constraints.setter
    def value_constraints(self, value_constraints):
        """Sets the value_constraints of this TaskFieldDefinition.


        :param value_constraints: The value_constraints of this TaskFieldDefinition.  # noqa: E501
        :type value_constraints: lusid_workflow.ValueConstraints
        """

        self._value_constraints = value_constraints

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
        if not isinstance(other, TaskFieldDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskFieldDefinition):
            return True

        return self.to_dict() != other.to_dict()
