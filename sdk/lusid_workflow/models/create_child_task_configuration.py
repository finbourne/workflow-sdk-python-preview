# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1223
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


class CreateChildTaskConfiguration(object):
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
        'task_definition_id': 'ResourceId',
        'task_definition_as_at': 'datetime',
        'initial_trigger': 'str',
        'child_task_fields': 'dict[str, FieldMapping]',
        'map_stacking_key_from': 'str'
    }

    attribute_map = {
        'task_definition_id': 'taskDefinitionId',
        'task_definition_as_at': 'taskDefinitionAsAt',
        'initial_trigger': 'initialTrigger',
        'child_task_fields': 'childTaskFields',
        'map_stacking_key_from': 'mapStackingKeyFrom'
    }

    required_map = {
        'task_definition_id': 'required',
        'task_definition_as_at': 'optional',
        'initial_trigger': 'optional',
        'child_task_fields': 'optional',
        'map_stacking_key_from': 'optional'
    }

    def __init__(self, task_definition_id=None, task_definition_as_at=None, initial_trigger=None, child_task_fields=None, map_stacking_key_from=None, local_vars_configuration=None):  # noqa: E501
        """CreateChildTaskConfiguration - a model defined in OpenAPI"
        
        :param task_definition_id:  (required)
        :type task_definition_id: lusid_workflow.ResourceId
        :param task_definition_as_at:  TaskDefinition AsAt timestamp
        :type task_definition_as_at: datetime
        :param initial_trigger:  The Initial Trigger for automatic start
        :type initial_trigger: str
        :param child_task_fields:  Field Mappings
        :type child_task_fields: dict[str, lusid_workflow.FieldMapping]
        :param map_stacking_key_from:  If present, the value of this field on the parent task will be the Stacking Key on any created child tasks
        :type map_stacking_key_from: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._task_definition_id = None
        self._task_definition_as_at = None
        self._initial_trigger = None
        self._child_task_fields = None
        self._map_stacking_key_from = None
        self.discriminator = None

        self.task_definition_id = task_definition_id
        self.task_definition_as_at = task_definition_as_at
        self.initial_trigger = initial_trigger
        self.child_task_fields = child_task_fields
        self.map_stacking_key_from = map_stacking_key_from

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this CreateChildTaskConfiguration.  # noqa: E501


        :return: The task_definition_id of this CreateChildTaskConfiguration.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this CreateChildTaskConfiguration.


        :param task_definition_id: The task_definition_id of this CreateChildTaskConfiguration.  # noqa: E501
        :type task_definition_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and task_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_id`, must not be `None`")  # noqa: E501

        self._task_definition_id = task_definition_id

    @property
    def task_definition_as_at(self):
        """Gets the task_definition_as_at of this CreateChildTaskConfiguration.  # noqa: E501

        TaskDefinition AsAt timestamp  # noqa: E501

        :return: The task_definition_as_at of this CreateChildTaskConfiguration.  # noqa: E501
        :rtype: datetime
        """
        return self._task_definition_as_at

    @task_definition_as_at.setter
    def task_definition_as_at(self, task_definition_as_at):
        """Sets the task_definition_as_at of this CreateChildTaskConfiguration.

        TaskDefinition AsAt timestamp  # noqa: E501

        :param task_definition_as_at: The task_definition_as_at of this CreateChildTaskConfiguration.  # noqa: E501
        :type task_definition_as_at: datetime
        """

        self._task_definition_as_at = task_definition_as_at

    @property
    def initial_trigger(self):
        """Gets the initial_trigger of this CreateChildTaskConfiguration.  # noqa: E501

        The Initial Trigger for automatic start  # noqa: E501

        :return: The initial_trigger of this CreateChildTaskConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._initial_trigger

    @initial_trigger.setter
    def initial_trigger(self, initial_trigger):
        """Sets the initial_trigger of this CreateChildTaskConfiguration.

        The Initial Trigger for automatic start  # noqa: E501

        :param initial_trigger: The initial_trigger of this CreateChildTaskConfiguration.  # noqa: E501
        :type initial_trigger: str
        """
        if (self.local_vars_configuration.client_side_validation and
                initial_trigger is not None and len(initial_trigger) > 1024):
            raise ValueError("Invalid value for `initial_trigger`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                initial_trigger is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', initial_trigger)):  # noqa: E501
            raise ValueError(r"Invalid value for `initial_trigger`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._initial_trigger = initial_trigger

    @property
    def child_task_fields(self):
        """Gets the child_task_fields of this CreateChildTaskConfiguration.  # noqa: E501

        Field Mappings  # noqa: E501

        :return: The child_task_fields of this CreateChildTaskConfiguration.  # noqa: E501
        :rtype: dict[str, lusid_workflow.FieldMapping]
        """
        return self._child_task_fields

    @child_task_fields.setter
    def child_task_fields(self, child_task_fields):
        """Sets the child_task_fields of this CreateChildTaskConfiguration.

        Field Mappings  # noqa: E501

        :param child_task_fields: The child_task_fields of this CreateChildTaskConfiguration.  # noqa: E501
        :type child_task_fields: dict[str, lusid_workflow.FieldMapping]
        """

        self._child_task_fields = child_task_fields

    @property
    def map_stacking_key_from(self):
        """Gets the map_stacking_key_from of this CreateChildTaskConfiguration.  # noqa: E501

        If present, the value of this field on the parent task will be the Stacking Key on any created child tasks  # noqa: E501

        :return: The map_stacking_key_from of this CreateChildTaskConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._map_stacking_key_from

    @map_stacking_key_from.setter
    def map_stacking_key_from(self, map_stacking_key_from):
        """Sets the map_stacking_key_from of this CreateChildTaskConfiguration.

        If present, the value of this field on the parent task will be the Stacking Key on any created child tasks  # noqa: E501

        :param map_stacking_key_from: The map_stacking_key_from of this CreateChildTaskConfiguration.  # noqa: E501
        :type map_stacking_key_from: str
        """

        self._map_stacking_key_from = map_stacking_key_from

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
        if not isinstance(other, CreateChildTaskConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateChildTaskConfiguration):
            return True

        return self.to_dict() != other.to_dict()
