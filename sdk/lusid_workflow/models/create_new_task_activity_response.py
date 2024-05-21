# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1043
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


class CreateNewTaskActivityResponse(object):
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
        'initial_trigger': 'str',
        'correlation_ids': 'list[EventHandlerMapping]',
        'task_fields': 'dict[str, FieldMapping]'
    }

    attribute_map = {
        'type': 'type',
        'initial_trigger': 'initialTrigger',
        'correlation_ids': 'correlationIds',
        'task_fields': 'taskFields'
    }

    required_map = {
        'type': 'optional',
        'initial_trigger': 'optional',
        'correlation_ids': 'optional',
        'task_fields': 'optional'
    }

    def __init__(self, type=None, initial_trigger=None, correlation_ids=None, task_fields=None, local_vars_configuration=None):  # noqa: E501
        """CreateNewTaskActivityResponse - a model defined in OpenAPI"
        
        :param type:  Type of task activity
        :type type: str
        :param initial_trigger:  Trigger to supply to all tasks to be made
        :type initial_trigger: str
        :param correlation_ids:  The event to correlation ID mappings
        :type correlation_ids: list[lusid_workflow.EventHandlerMapping]
        :param task_fields:  The event to task field mappings
        :type task_fields: dict[str, lusid_workflow.FieldMapping]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._initial_trigger = None
        self._correlation_ids = None
        self._task_fields = None
        self.discriminator = None

        self.type = type
        self.initial_trigger = initial_trigger
        self.correlation_ids = correlation_ids
        self.task_fields = task_fields

    @property
    def type(self):
        """Gets the type of this CreateNewTaskActivityResponse.  # noqa: E501

        Type of task activity  # noqa: E501

        :return: The type of this CreateNewTaskActivityResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateNewTaskActivityResponse.

        Type of task activity  # noqa: E501

        :param type: The type of this CreateNewTaskActivityResponse.  # noqa: E501
        :type type: str
        """
        allowed_values = [None,"CreateNewTask"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def initial_trigger(self):
        """Gets the initial_trigger of this CreateNewTaskActivityResponse.  # noqa: E501

        Trigger to supply to all tasks to be made  # noqa: E501

        :return: The initial_trigger of this CreateNewTaskActivityResponse.  # noqa: E501
        :rtype: str
        """
        return self._initial_trigger

    @initial_trigger.setter
    def initial_trigger(self, initial_trigger):
        """Sets the initial_trigger of this CreateNewTaskActivityResponse.

        Trigger to supply to all tasks to be made  # noqa: E501

        :param initial_trigger: The initial_trigger of this CreateNewTaskActivityResponse.  # noqa: E501
        :type initial_trigger: str
        """

        self._initial_trigger = initial_trigger

    @property
    def correlation_ids(self):
        """Gets the correlation_ids of this CreateNewTaskActivityResponse.  # noqa: E501

        The event to correlation ID mappings  # noqa: E501

        :return: The correlation_ids of this CreateNewTaskActivityResponse.  # noqa: E501
        :rtype: list[lusid_workflow.EventHandlerMapping]
        """
        return self._correlation_ids

    @correlation_ids.setter
    def correlation_ids(self, correlation_ids):
        """Sets the correlation_ids of this CreateNewTaskActivityResponse.

        The event to correlation ID mappings  # noqa: E501

        :param correlation_ids: The correlation_ids of this CreateNewTaskActivityResponse.  # noqa: E501
        :type correlation_ids: list[lusid_workflow.EventHandlerMapping]
        """

        self._correlation_ids = correlation_ids

    @property
    def task_fields(self):
        """Gets the task_fields of this CreateNewTaskActivityResponse.  # noqa: E501

        The event to task field mappings  # noqa: E501

        :return: The task_fields of this CreateNewTaskActivityResponse.  # noqa: E501
        :rtype: dict[str, lusid_workflow.FieldMapping]
        """
        return self._task_fields

    @task_fields.setter
    def task_fields(self, task_fields):
        """Sets the task_fields of this CreateNewTaskActivityResponse.

        The event to task field mappings  # noqa: E501

        :param task_fields: The task_fields of this CreateNewTaskActivityResponse.  # noqa: E501
        :type task_fields: dict[str, lusid_workflow.FieldMapping]
        """

        self._task_fields = task_fields

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
        if not isinstance(other, CreateNewTaskActivityResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNewTaskActivityResponse):
            return True

        return self.to_dict() != other.to_dict()
