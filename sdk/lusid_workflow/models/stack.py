# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.587
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


class Stack(object):
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
        'member_added_as_at': 'datetime',
        'stack_opened_as_at': 'datetime',
        'stack_closed_as_at': 'datetime',
        'stack_membership_type': 'str',
        'stack_status': 'str',
        'lead_task_id': 'str',
        'lead_task_state': 'str',
        'tasks_in_stack': 'int'
    }

    attribute_map = {
        'member_added_as_at': 'memberAddedAsAt',
        'stack_opened_as_at': 'stackOpenedAsAt',
        'stack_closed_as_at': 'stackClosedAsAt',
        'stack_membership_type': 'stackMembershipType',
        'stack_status': 'stackStatus',
        'lead_task_id': 'leadTaskId',
        'lead_task_state': 'leadTaskState',
        'tasks_in_stack': 'tasksInStack'
    }

    required_map = {
        'member_added_as_at': 'optional',
        'stack_opened_as_at': 'optional',
        'stack_closed_as_at': 'optional',
        'stack_membership_type': 'optional',
        'stack_status': 'optional',
        'lead_task_id': 'optional',
        'lead_task_state': 'optional',
        'tasks_in_stack': 'optional'
    }

    def __init__(self, member_added_as_at=None, stack_opened_as_at=None, stack_closed_as_at=None, stack_membership_type=None, stack_status=None, lead_task_id=None, lead_task_state=None, tasks_in_stack=None, local_vars_configuration=None):  # noqa: E501
        """Stack - a model defined in OpenAPI"
        
        :param member_added_as_at:  When the Task was added to the Stack
        :type member_added_as_at: datetime
        :param stack_opened_as_at:  When the Stack was opened
        :type stack_opened_as_at: datetime
        :param stack_closed_as_at:  When the Stack was closed
        :type stack_closed_as_at: datetime
        :param stack_membership_type:  Whether the task is the Lead task of the Stack or a Member within the Stack
        :type stack_membership_type: str
        :param stack_status:  Status of the Stack (Open/Closed)
        :type stack_status: str
        :param lead_task_id:  ID of the Lead Task
        :type lead_task_id: str
        :param lead_task_state:  State of the Lead Task
        :type lead_task_state: str
        :param tasks_in_stack:  Number of Tasks in the Stack
        :type tasks_in_stack: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._member_added_as_at = None
        self._stack_opened_as_at = None
        self._stack_closed_as_at = None
        self._stack_membership_type = None
        self._stack_status = None
        self._lead_task_id = None
        self._lead_task_state = None
        self._tasks_in_stack = None
        self.discriminator = None

        if member_added_as_at is not None:
            self.member_added_as_at = member_added_as_at
        if stack_opened_as_at is not None:
            self.stack_opened_as_at = stack_opened_as_at
        self.stack_closed_as_at = stack_closed_as_at
        self.stack_membership_type = stack_membership_type
        self.stack_status = stack_status
        if lead_task_id is not None:
            self.lead_task_id = lead_task_id
        self.lead_task_state = lead_task_state
        if tasks_in_stack is not None:
            self.tasks_in_stack = tasks_in_stack

    @property
    def member_added_as_at(self):
        """Gets the member_added_as_at of this Stack.  # noqa: E501

        When the Task was added to the Stack  # noqa: E501

        :return: The member_added_as_at of this Stack.  # noqa: E501
        :rtype: datetime
        """
        return self._member_added_as_at

    @member_added_as_at.setter
    def member_added_as_at(self, member_added_as_at):
        """Sets the member_added_as_at of this Stack.

        When the Task was added to the Stack  # noqa: E501

        :param member_added_as_at: The member_added_as_at of this Stack.  # noqa: E501
        :type member_added_as_at: datetime
        """

        self._member_added_as_at = member_added_as_at

    @property
    def stack_opened_as_at(self):
        """Gets the stack_opened_as_at of this Stack.  # noqa: E501

        When the Stack was opened  # noqa: E501

        :return: The stack_opened_as_at of this Stack.  # noqa: E501
        :rtype: datetime
        """
        return self._stack_opened_as_at

    @stack_opened_as_at.setter
    def stack_opened_as_at(self, stack_opened_as_at):
        """Sets the stack_opened_as_at of this Stack.

        When the Stack was opened  # noqa: E501

        :param stack_opened_as_at: The stack_opened_as_at of this Stack.  # noqa: E501
        :type stack_opened_as_at: datetime
        """

        self._stack_opened_as_at = stack_opened_as_at

    @property
    def stack_closed_as_at(self):
        """Gets the stack_closed_as_at of this Stack.  # noqa: E501

        When the Stack was closed  # noqa: E501

        :return: The stack_closed_as_at of this Stack.  # noqa: E501
        :rtype: datetime
        """
        return self._stack_closed_as_at

    @stack_closed_as_at.setter
    def stack_closed_as_at(self, stack_closed_as_at):
        """Sets the stack_closed_as_at of this Stack.

        When the Stack was closed  # noqa: E501

        :param stack_closed_as_at: The stack_closed_as_at of this Stack.  # noqa: E501
        :type stack_closed_as_at: datetime
        """

        self._stack_closed_as_at = stack_closed_as_at

    @property
    def stack_membership_type(self):
        """Gets the stack_membership_type of this Stack.  # noqa: E501

        Whether the task is the Lead task of the Stack or a Member within the Stack  # noqa: E501

        :return: The stack_membership_type of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._stack_membership_type

    @stack_membership_type.setter
    def stack_membership_type(self, stack_membership_type):
        """Sets the stack_membership_type of this Stack.

        Whether the task is the Lead task of the Stack or a Member within the Stack  # noqa: E501

        :param stack_membership_type: The stack_membership_type of this Stack.  # noqa: E501
        :type stack_membership_type: str
        """

        self._stack_membership_type = stack_membership_type

    @property
    def stack_status(self):
        """Gets the stack_status of this Stack.  # noqa: E501

        Status of the Stack (Open/Closed)  # noqa: E501

        :return: The stack_status of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._stack_status

    @stack_status.setter
    def stack_status(self, stack_status):
        """Sets the stack_status of this Stack.

        Status of the Stack (Open/Closed)  # noqa: E501

        :param stack_status: The stack_status of this Stack.  # noqa: E501
        :type stack_status: str
        """

        self._stack_status = stack_status

    @property
    def lead_task_id(self):
        """Gets the lead_task_id of this Stack.  # noqa: E501

        ID of the Lead Task  # noqa: E501

        :return: The lead_task_id of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._lead_task_id

    @lead_task_id.setter
    def lead_task_id(self, lead_task_id):
        """Sets the lead_task_id of this Stack.

        ID of the Lead Task  # noqa: E501

        :param lead_task_id: The lead_task_id of this Stack.  # noqa: E501
        :type lead_task_id: str
        """

        self._lead_task_id = lead_task_id

    @property
    def lead_task_state(self):
        """Gets the lead_task_state of this Stack.  # noqa: E501

        State of the Lead Task  # noqa: E501

        :return: The lead_task_state of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._lead_task_state

    @lead_task_state.setter
    def lead_task_state(self, lead_task_state):
        """Sets the lead_task_state of this Stack.

        State of the Lead Task  # noqa: E501

        :param lead_task_state: The lead_task_state of this Stack.  # noqa: E501
        :type lead_task_state: str
        """

        self._lead_task_state = lead_task_state

    @property
    def tasks_in_stack(self):
        """Gets the tasks_in_stack of this Stack.  # noqa: E501

        Number of Tasks in the Stack  # noqa: E501

        :return: The tasks_in_stack of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._tasks_in_stack

    @tasks_in_stack.setter
    def tasks_in_stack(self, tasks_in_stack):
        """Sets the tasks_in_stack of this Stack.

        Number of Tasks in the Stack  # noqa: E501

        :param tasks_in_stack: The tasks_in_stack of this Stack.  # noqa: E501
        :type tasks_in_stack: int
        """

        self._tasks_in_stack = tasks_in_stack

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
        if not isinstance(other, Stack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Stack):
            return True

        return self.to_dict() != other.to_dict()
