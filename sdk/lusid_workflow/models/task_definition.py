# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.963
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


class TaskDefinition(object):
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
        'id': 'ResourceId',
        'version': 'VersionInfo',
        'display_name': 'str',
        'description': 'str',
        'states': 'list[TaskStateDefinition]',
        'field_schema': 'list[TaskFieldDefinition]',
        'initial_state': 'InitialState',
        'triggers': 'list[TransitionTriggerDefinition]',
        'actions': 'list[ActionDefinitionResponse]',
        'transitions': 'list[TaskTransitionDefinition]'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'states': 'states',
        'field_schema': 'fieldSchema',
        'initial_state': 'initialState',
        'triggers': 'triggers',
        'actions': 'actions',
        'transitions': 'transitions'
    }

    required_map = {
        'id': 'required',
        'version': 'optional',
        'display_name': 'required',
        'description': 'optional',
        'states': 'required',
        'field_schema': 'optional',
        'initial_state': 'required',
        'triggers': 'optional',
        'actions': 'optional',
        'transitions': 'optional'
    }

    def __init__(self, id=None, version=None, display_name=None, description=None, states=None, field_schema=None, initial_state=None, triggers=None, actions=None, transitions=None, local_vars_configuration=None):  # noqa: E501
        """TaskDefinition - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_workflow.ResourceId
        :param version: 
        :type version: lusid_workflow.VersionInfo
        :param display_name:  Human readable name (required)
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param states:  The states this Task Definition operates over (required)
        :type states: list[lusid_workflow.TaskStateDefinition]
        :param field_schema:  The Fields that this Task Definition operates on
        :type field_schema: list[lusid_workflow.TaskFieldDefinition]
        :param initial_state:  (required)
        :type initial_state: lusid_workflow.InitialState
        :param triggers:  The Triggers for State transition
        :type triggers: list[lusid_workflow.TransitionTriggerDefinition]
        :param actions:  The Actions of this Task - executed after a Transition completion
        :type actions: list[lusid_workflow.ActionDefinitionResponse]
        :param transitions:  The Transitions between States
        :type transitions: list[lusid_workflow.TaskTransitionDefinition]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._display_name = None
        self._description = None
        self._states = None
        self._field_schema = None
        self._initial_state = None
        self._triggers = None
        self._actions = None
        self._transitions = None
        self.discriminator = None

        self.id = id
        if version is not None:
            self.version = version
        self.display_name = display_name
        self.description = description
        self.states = states
        self.field_schema = field_schema
        self.initial_state = initial_state
        self.triggers = triggers
        self.actions = actions
        self.transitions = transitions

    @property
    def id(self):
        """Gets the id of this TaskDefinition.  # noqa: E501


        :return: The id of this TaskDefinition.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDefinition.


        :param id: The id of this TaskDefinition.  # noqa: E501
        :type id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this TaskDefinition.  # noqa: E501


        :return: The version of this TaskDefinition.  # noqa: E501
        :rtype: lusid_workflow.VersionInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TaskDefinition.


        :param version: The version of this TaskDefinition.  # noqa: E501
        :type version: lusid_workflow.VersionInfo
        """

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this TaskDefinition.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this TaskDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TaskDefinition.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this TaskDefinition.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this TaskDefinition.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this TaskDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDefinition.

        Human readable description  # noqa: E501

        :param description: The description of this TaskDefinition.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def states(self):
        """Gets the states of this TaskDefinition.  # noqa: E501

        The states this Task Definition operates over  # noqa: E501

        :return: The states of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.TaskStateDefinition]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this TaskDefinition.

        The states this Task Definition operates over  # noqa: E501

        :param states: The states of this TaskDefinition.  # noqa: E501
        :type states: list[lusid_workflow.TaskStateDefinition]
        """
        if self.local_vars_configuration.client_side_validation and states is None:  # noqa: E501
            raise ValueError("Invalid value for `states`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                states is not None and len(states) < 1):
            raise ValueError("Invalid value for `states`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._states = states

    @property
    def field_schema(self):
        """Gets the field_schema of this TaskDefinition.  # noqa: E501

        The Fields that this Task Definition operates on  # noqa: E501

        :return: The field_schema of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.TaskFieldDefinition]
        """
        return self._field_schema

    @field_schema.setter
    def field_schema(self, field_schema):
        """Sets the field_schema of this TaskDefinition.

        The Fields that this Task Definition operates on  # noqa: E501

        :param field_schema: The field_schema of this TaskDefinition.  # noqa: E501
        :type field_schema: list[lusid_workflow.TaskFieldDefinition]
        """

        self._field_schema = field_schema

    @property
    def initial_state(self):
        """Gets the initial_state of this TaskDefinition.  # noqa: E501


        :return: The initial_state of this TaskDefinition.  # noqa: E501
        :rtype: lusid_workflow.InitialState
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state):
        """Sets the initial_state of this TaskDefinition.


        :param initial_state: The initial_state of this TaskDefinition.  # noqa: E501
        :type initial_state: lusid_workflow.InitialState
        """
        if self.local_vars_configuration.client_side_validation and initial_state is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_state`, must not be `None`")  # noqa: E501

        self._initial_state = initial_state

    @property
    def triggers(self):
        """Gets the triggers of this TaskDefinition.  # noqa: E501

        The Triggers for State transition  # noqa: E501

        :return: The triggers of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.TransitionTriggerDefinition]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this TaskDefinition.

        The Triggers for State transition  # noqa: E501

        :param triggers: The triggers of this TaskDefinition.  # noqa: E501
        :type triggers: list[lusid_workflow.TransitionTriggerDefinition]
        """

        self._triggers = triggers

    @property
    def actions(self):
        """Gets the actions of this TaskDefinition.  # noqa: E501

        The Actions of this Task - executed after a Transition completion  # noqa: E501

        :return: The actions of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.ActionDefinitionResponse]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this TaskDefinition.

        The Actions of this Task - executed after a Transition completion  # noqa: E501

        :param actions: The actions of this TaskDefinition.  # noqa: E501
        :type actions: list[lusid_workflow.ActionDefinitionResponse]
        """

        self._actions = actions

    @property
    def transitions(self):
        """Gets the transitions of this TaskDefinition.  # noqa: E501

        The Transitions between States  # noqa: E501

        :return: The transitions of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.TaskTransitionDefinition]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """Sets the transitions of this TaskDefinition.

        The Transitions between States  # noqa: E501

        :param transitions: The transitions of this TaskDefinition.  # noqa: E501
        :type transitions: list[lusid_workflow.TaskTransitionDefinition]
        """

        self._transitions = transitions

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
        if not isinstance(other, TaskDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDefinition):
            return True

        return self.to_dict() != other.to_dict()
