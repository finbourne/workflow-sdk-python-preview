# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1021
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


class TaskSummary(object):
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
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_definition_id': 'taskDefinitionId',
        'task_definition_version': 'taskDefinitionVersion',
        'task_definition_display_name': 'taskDefinitionDisplayName',
        'state': 'state'
    }

    required_map = {
        'id': 'required',
        'task_definition_id': 'required',
        'task_definition_version': 'required',
        'task_definition_display_name': 'required',
        'state': 'required'
    }

    def __init__(self, id=None, task_definition_id=None, task_definition_version=None, task_definition_display_name=None, state=None, local_vars_configuration=None):  # noqa: E501
        """TaskSummary - a model defined in OpenAPI"
        
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

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._task_definition_id = None
        self._task_definition_version = None
        self._task_definition_display_name = None
        self._state = None
        self.discriminator = None

        self.id = id
        self.task_definition_id = task_definition_id
        self.task_definition_version = task_definition_version
        self.task_definition_display_name = task_definition_display_name
        self.state = state

    @property
    def id(self):
        """Gets the id of this TaskSummary.  # noqa: E501

        The unique id for this Task  # noqa: E501

        :return: The id of this TaskSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskSummary.

        The unique id for this Task  # noqa: E501

        :param id: The id of this TaskSummary.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this TaskSummary.  # noqa: E501


        :return: The task_definition_id of this TaskSummary.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this TaskSummary.


        :param task_definition_id: The task_definition_id of this TaskSummary.  # noqa: E501
        :type task_definition_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and task_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_id`, must not be `None`")  # noqa: E501

        self._task_definition_id = task_definition_id

    @property
    def task_definition_version(self):
        """Gets the task_definition_version of this TaskSummary.  # noqa: E501


        :return: The task_definition_version of this TaskSummary.  # noqa: E501
        :rtype: lusid_workflow.TaskDefinitionVersion
        """
        return self._task_definition_version

    @task_definition_version.setter
    def task_definition_version(self, task_definition_version):
        """Sets the task_definition_version of this TaskSummary.


        :param task_definition_version: The task_definition_version of this TaskSummary.  # noqa: E501
        :type task_definition_version: lusid_workflow.TaskDefinitionVersion
        """
        if self.local_vars_configuration.client_side_validation and task_definition_version is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_version`, must not be `None`")  # noqa: E501

        self._task_definition_version = task_definition_version

    @property
    def task_definition_display_name(self):
        """Gets the task_definition_display_name of this TaskSummary.  # noqa: E501

        The display name of the Task Definition used by this Task  # noqa: E501

        :return: The task_definition_display_name of this TaskSummary.  # noqa: E501
        :rtype: str
        """
        return self._task_definition_display_name

    @task_definition_display_name.setter
    def task_definition_display_name(self, task_definition_display_name):
        """Sets the task_definition_display_name of this TaskSummary.

        The display name of the Task Definition used by this Task  # noqa: E501

        :param task_definition_display_name: The task_definition_display_name of this TaskSummary.  # noqa: E501
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
        """Gets the state of this TaskSummary.  # noqa: E501

        Current State  # noqa: E501

        :return: The state of this TaskSummary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskSummary.

        Current State  # noqa: E501

        :param state: The state of this TaskSummary.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 1):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, TaskSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskSummary):
            return True

        return self.to_dict() != other.to_dict()
