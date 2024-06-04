# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1089
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


class Task(object):
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
        'id': 'str',
        'task_definition_id': 'ResourceId',
        'task_definition_version': 'TaskDefinitionVersion',
        'task_definition_display_name': 'str',
        'state': 'str',
        'ultimate_parent_task': 'TaskSummary',
        'parent_task': 'TaskSummary',
        'child_tasks': 'list[TaskSummary]',
        'correlation_ids': 'list[str]',
        'version': 'VersionInfo',
        'terminal_state': 'bool',
        'as_at_last_transition': 'datetime',
        'fields': 'list[TaskInstanceField]',
        'stacking_key': 'str',
        'stack': 'Stack'
    }

    attribute_map = {
        'id': 'id',
        'task_definition_id': 'taskDefinitionId',
        'task_definition_version': 'taskDefinitionVersion',
        'task_definition_display_name': 'taskDefinitionDisplayName',
        'state': 'state',
        'ultimate_parent_task': 'ultimateParentTask',
        'parent_task': 'parentTask',
        'child_tasks': 'childTasks',
        'correlation_ids': 'correlationIds',
        'version': 'version',
        'terminal_state': 'terminalState',
        'as_at_last_transition': 'asAtLastTransition',
        'fields': 'fields',
        'stacking_key': 'stackingKey',
        'stack': 'stack'
    }

    required_map = {
        'id': 'required',
        'task_definition_id': 'required',
        'task_definition_version': 'required',
        'task_definition_display_name': 'required',
        'state': 'required',
        'ultimate_parent_task': 'required',
        'parent_task': 'optional',
        'child_tasks': 'optional',
        'correlation_ids': 'optional',
        'version': 'optional',
        'terminal_state': 'required',
        'as_at_last_transition': 'optional',
        'fields': 'optional',
        'stacking_key': 'optional',
        'stack': 'optional'
    }

    def __init__(self, id=None, task_definition_id=None, task_definition_version=None, task_definition_display_name=None, state=None, ultimate_parent_task=None, parent_task=None, child_tasks=None, correlation_ids=None, version=None, terminal_state=None, as_at_last_transition=None, fields=None, stacking_key=None, stack=None, local_vars_configuration=None):  # noqa: E501
        """Task - a model defined in OpenAPI"
        
        :param id:  The unique id for this Task (required)
        :type id: str
        :param task_definition_id:  (required)
        :type task_definition_id: lusid_workflow.ResourceId
        :param task_definition_version:  (required)
        :type task_definition_version: lusid_workflow.TaskDefinitionVersion
        :param task_definition_display_name:  The display name of the Task Definition used by this Task (required)
        :type task_definition_display_name: str
        :param state:  Current State (required)
        :type state: str
        :param ultimate_parent_task:  (required)
        :type ultimate_parent_task: lusid_workflow.TaskSummary
        :param parent_task: 
        :type parent_task: lusid_workflow.TaskSummary
        :param child_tasks:  This Task's child tasks
        :type child_tasks: list[lusid_workflow.TaskSummary]
        :param correlation_ids:  User-provided ID used to link entities and tasks
        :type correlation_ids: list[str]
        :param version: 
        :type version: lusid_workflow.VersionInfo
        :param terminal_state:  True if no onward transitions are possible (required)
        :type terminal_state: bool
        :param as_at_last_transition:  Last Transition timestamp
        :type as_at_last_transition: datetime
        :param fields:  Fields and their latest values - should correspond with the Task Definition field schema
        :type fields: list[lusid_workflow.TaskInstanceField]
        :param stacking_key:  The key used to determine which stack to add the Task to
        :type stacking_key: str
        :param stack: 
        :type stack: lusid_workflow.Stack

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._task_definition_id = None
        self._task_definition_version = None
        self._task_definition_display_name = None
        self._state = None
        self._ultimate_parent_task = None
        self._parent_task = None
        self._child_tasks = None
        self._correlation_ids = None
        self._version = None
        self._terminal_state = None
        self._as_at_last_transition = None
        self._fields = None
        self._stacking_key = None
        self._stack = None
        self.discriminator = None

        self.id = id
        self.task_definition_id = task_definition_id
        self.task_definition_version = task_definition_version
        self.task_definition_display_name = task_definition_display_name
        self.state = state
        self.ultimate_parent_task = ultimate_parent_task
        if parent_task is not None:
            self.parent_task = parent_task
        self.child_tasks = child_tasks
        self.correlation_ids = correlation_ids
        if version is not None:
            self.version = version
        self.terminal_state = terminal_state
        self.as_at_last_transition = as_at_last_transition
        self.fields = fields
        self.stacking_key = stacking_key
        if stack is not None:
            self.stack = stack

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501

        The unique id for this Task  # noqa: E501

        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        The unique id for this Task  # noqa: E501

        :param id: The id of this Task.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this Task.  # noqa: E501


        :return: The task_definition_id of this Task.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this Task.


        :param task_definition_id: The task_definition_id of this Task.  # noqa: E501
        :type task_definition_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and task_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_id`, must not be `None`")  # noqa: E501

        self._task_definition_id = task_definition_id

    @property
    def task_definition_version(self):
        """Gets the task_definition_version of this Task.  # noqa: E501


        :return: The task_definition_version of this Task.  # noqa: E501
        :rtype: lusid_workflow.TaskDefinitionVersion
        """
        return self._task_definition_version

    @task_definition_version.setter
    def task_definition_version(self, task_definition_version):
        """Sets the task_definition_version of this Task.


        :param task_definition_version: The task_definition_version of this Task.  # noqa: E501
        :type task_definition_version: lusid_workflow.TaskDefinitionVersion
        """
        if self.local_vars_configuration.client_side_validation and task_definition_version is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_version`, must not be `None`")  # noqa: E501

        self._task_definition_version = task_definition_version

    @property
    def task_definition_display_name(self):
        """Gets the task_definition_display_name of this Task.  # noqa: E501

        The display name of the Task Definition used by this Task  # noqa: E501

        :return: The task_definition_display_name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._task_definition_display_name

    @task_definition_display_name.setter
    def task_definition_display_name(self, task_definition_display_name):
        """Sets the task_definition_display_name of this Task.

        The display name of the Task Definition used by this Task  # noqa: E501

        :param task_definition_display_name: The task_definition_display_name of this Task.  # noqa: E501
        :type task_definition_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and task_definition_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                task_definition_display_name is not None and len(task_definition_display_name) < 1):
            raise ValueError("Invalid value for `task_definition_display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._task_definition_display_name = task_definition_display_name

    @property
    def state(self):
        """Gets the state of this Task.  # noqa: E501

        Current State  # noqa: E501

        :return: The state of this Task.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Task.

        Current State  # noqa: E501

        :param state: The state of this Task.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 1):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

    @property
    def ultimate_parent_task(self):
        """Gets the ultimate_parent_task of this Task.  # noqa: E501


        :return: The ultimate_parent_task of this Task.  # noqa: E501
        :rtype: lusid_workflow.TaskSummary
        """
        return self._ultimate_parent_task

    @ultimate_parent_task.setter
    def ultimate_parent_task(self, ultimate_parent_task):
        """Sets the ultimate_parent_task of this Task.


        :param ultimate_parent_task: The ultimate_parent_task of this Task.  # noqa: E501
        :type ultimate_parent_task: lusid_workflow.TaskSummary
        """
        if self.local_vars_configuration.client_side_validation and ultimate_parent_task is None:  # noqa: E501
            raise ValueError("Invalid value for `ultimate_parent_task`, must not be `None`")  # noqa: E501

        self._ultimate_parent_task = ultimate_parent_task

    @property
    def parent_task(self):
        """Gets the parent_task of this Task.  # noqa: E501


        :return: The parent_task of this Task.  # noqa: E501
        :rtype: lusid_workflow.TaskSummary
        """
        return self._parent_task

    @parent_task.setter
    def parent_task(self, parent_task):
        """Sets the parent_task of this Task.


        :param parent_task: The parent_task of this Task.  # noqa: E501
        :type parent_task: lusid_workflow.TaskSummary
        """

        self._parent_task = parent_task

    @property
    def child_tasks(self):
        """Gets the child_tasks of this Task.  # noqa: E501

        This Task's child tasks  # noqa: E501

        :return: The child_tasks of this Task.  # noqa: E501
        :rtype: list[lusid_workflow.TaskSummary]
        """
        return self._child_tasks

    @child_tasks.setter
    def child_tasks(self, child_tasks):
        """Sets the child_tasks of this Task.

        This Task's child tasks  # noqa: E501

        :param child_tasks: The child_tasks of this Task.  # noqa: E501
        :type child_tasks: list[lusid_workflow.TaskSummary]
        """

        self._child_tasks = child_tasks

    @property
    def correlation_ids(self):
        """Gets the correlation_ids of this Task.  # noqa: E501

        User-provided ID used to link entities and tasks  # noqa: E501

        :return: The correlation_ids of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._correlation_ids

    @correlation_ids.setter
    def correlation_ids(self, correlation_ids):
        """Sets the correlation_ids of this Task.

        User-provided ID used to link entities and tasks  # noqa: E501

        :param correlation_ids: The correlation_ids of this Task.  # noqa: E501
        :type correlation_ids: list[str]
        """

        self._correlation_ids = correlation_ids

    @property
    def version(self):
        """Gets the version of this Task.  # noqa: E501


        :return: The version of this Task.  # noqa: E501
        :rtype: lusid_workflow.VersionInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Task.


        :param version: The version of this Task.  # noqa: E501
        :type version: lusid_workflow.VersionInfo
        """

        self._version = version

    @property
    def terminal_state(self):
        """Gets the terminal_state of this Task.  # noqa: E501

        True if no onward transitions are possible  # noqa: E501

        :return: The terminal_state of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._terminal_state

    @terminal_state.setter
    def terminal_state(self, terminal_state):
        """Sets the terminal_state of this Task.

        True if no onward transitions are possible  # noqa: E501

        :param terminal_state: The terminal_state of this Task.  # noqa: E501
        :type terminal_state: bool
        """
        if self.local_vars_configuration.client_side_validation and terminal_state is None:  # noqa: E501
            raise ValueError("Invalid value for `terminal_state`, must not be `None`")  # noqa: E501

        self._terminal_state = terminal_state

    @property
    def as_at_last_transition(self):
        """Gets the as_at_last_transition of this Task.  # noqa: E501

        Last Transition timestamp  # noqa: E501

        :return: The as_at_last_transition of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_last_transition

    @as_at_last_transition.setter
    def as_at_last_transition(self, as_at_last_transition):
        """Sets the as_at_last_transition of this Task.

        Last Transition timestamp  # noqa: E501

        :param as_at_last_transition: The as_at_last_transition of this Task.  # noqa: E501
        :type as_at_last_transition: datetime
        """

        self._as_at_last_transition = as_at_last_transition

    @property
    def fields(self):
        """Gets the fields of this Task.  # noqa: E501

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :return: The fields of this Task.  # noqa: E501
        :rtype: list[lusid_workflow.TaskInstanceField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Task.

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :param fields: The fields of this Task.  # noqa: E501
        :type fields: list[lusid_workflow.TaskInstanceField]
        """

        self._fields = fields

    @property
    def stacking_key(self):
        """Gets the stacking_key of this Task.  # noqa: E501

        The key used to determine which stack to add the Task to  # noqa: E501

        :return: The stacking_key of this Task.  # noqa: E501
        :rtype: str
        """
        return self._stacking_key

    @stacking_key.setter
    def stacking_key(self, stacking_key):
        """Sets the stacking_key of this Task.

        The key used to determine which stack to add the Task to  # noqa: E501

        :param stacking_key: The stacking_key of this Task.  # noqa: E501
        :type stacking_key: str
        """

        self._stacking_key = stacking_key

    @property
    def stack(self):
        """Gets the stack of this Task.  # noqa: E501


        :return: The stack of this Task.  # noqa: E501
        :rtype: lusid_workflow.Stack
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """Sets the stack of this Task.


        :param stack: The stack of this Task.  # noqa: E501
        :type stack: lusid_workflow.Stack
        """

        self._stack = stack

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
        if not isinstance(other, Task):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Task):
            return True

        return self.to_dict() != other.to_dict()
