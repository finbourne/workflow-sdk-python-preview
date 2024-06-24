# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1143
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


class EventHandler(object):
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
        'status': 'str',
        'event_matching_pattern': 'EventMatchingPattern',
        'run_as_user_id': 'EventHandlerMapping',
        'task_definition_id': 'ResourceId',
        'task_definition_as_at': 'datetime',
        'task_activity': 'TaskActivityResponse'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'status': 'status',
        'event_matching_pattern': 'eventMatchingPattern',
        'run_as_user_id': 'runAsUserId',
        'task_definition_id': 'taskDefinitionId',
        'task_definition_as_at': 'taskDefinitionAsAt',
        'task_activity': 'taskActivity'
    }

    required_map = {
        'id': 'required',
        'version': 'optional',
        'display_name': 'required',
        'description': 'optional',
        'status': 'required',
        'event_matching_pattern': 'required',
        'run_as_user_id': 'required',
        'task_definition_id': 'required',
        'task_definition_as_at': 'optional',
        'task_activity': 'required'
    }

    def __init__(self, id=None, version=None, display_name=None, description=None, status=None, event_matching_pattern=None, run_as_user_id=None, task_definition_id=None, task_definition_as_at=None, task_activity=None, local_vars_configuration=None):  # noqa: E501
        """EventHandler - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_workflow.ResourceId
        :param version: 
        :type version: lusid_workflow.VersionInfo
        :param display_name:  Human readable name (required)
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param status:  The current status of the event handler (required)
        :type status: str
        :param event_matching_pattern:  (required)
        :type event_matching_pattern: lusid_workflow.EventMatchingPattern
        :param run_as_user_id:  (required)
        :type run_as_user_id: lusid_workflow.EventHandlerMapping
        :param task_definition_id:  (required)
        :type task_definition_id: lusid_workflow.ResourceId
        :param task_definition_as_at:  AsAt of the required task definition
        :type task_definition_as_at: datetime
        :param task_activity:  (required)
        :type task_activity: lusid_workflow.TaskActivityResponse

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._display_name = None
        self._description = None
        self._status = None
        self._event_matching_pattern = None
        self._run_as_user_id = None
        self._task_definition_id = None
        self._task_definition_as_at = None
        self._task_activity = None
        self.discriminator = None

        self.id = id
        if version is not None:
            self.version = version
        self.display_name = display_name
        self.description = description
        self.status = status
        self.event_matching_pattern = event_matching_pattern
        self.run_as_user_id = run_as_user_id
        self.task_definition_id = task_definition_id
        self.task_definition_as_at = task_definition_as_at
        self.task_activity = task_activity

    @property
    def id(self):
        """Gets the id of this EventHandler.  # noqa: E501


        :return: The id of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventHandler.


        :param id: The id of this EventHandler.  # noqa: E501
        :type id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this EventHandler.  # noqa: E501


        :return: The version of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.VersionInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EventHandler.


        :param version: The version of this EventHandler.  # noqa: E501
        :type version: lusid_workflow.VersionInfo
        """

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this EventHandler.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EventHandler.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this EventHandler.  # noqa: E501
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
        """Gets the description of this EventHandler.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventHandler.

        Human readable description  # noqa: E501

        :param description: The description of this EventHandler.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this EventHandler.  # noqa: E501

        The current status of the event handler  # noqa: E501

        :return: The status of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventHandler.

        The current status of the event handler  # noqa: E501

        :param status: The status of this EventHandler.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def event_matching_pattern(self):
        """Gets the event_matching_pattern of this EventHandler.  # noqa: E501


        :return: The event_matching_pattern of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.EventMatchingPattern
        """
        return self._event_matching_pattern

    @event_matching_pattern.setter
    def event_matching_pattern(self, event_matching_pattern):
        """Sets the event_matching_pattern of this EventHandler.


        :param event_matching_pattern: The event_matching_pattern of this EventHandler.  # noqa: E501
        :type event_matching_pattern: lusid_workflow.EventMatchingPattern
        """
        if self.local_vars_configuration.client_side_validation and event_matching_pattern is None:  # noqa: E501
            raise ValueError("Invalid value for `event_matching_pattern`, must not be `None`")  # noqa: E501

        self._event_matching_pattern = event_matching_pattern

    @property
    def run_as_user_id(self):
        """Gets the run_as_user_id of this EventHandler.  # noqa: E501


        :return: The run_as_user_id of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.EventHandlerMapping
        """
        return self._run_as_user_id

    @run_as_user_id.setter
    def run_as_user_id(self, run_as_user_id):
        """Sets the run_as_user_id of this EventHandler.


        :param run_as_user_id: The run_as_user_id of this EventHandler.  # noqa: E501
        :type run_as_user_id: lusid_workflow.EventHandlerMapping
        """
        if self.local_vars_configuration.client_side_validation and run_as_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_as_user_id`, must not be `None`")  # noqa: E501

        self._run_as_user_id = run_as_user_id

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this EventHandler.  # noqa: E501


        :return: The task_definition_id of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this EventHandler.


        :param task_definition_id: The task_definition_id of this EventHandler.  # noqa: E501
        :type task_definition_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and task_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_definition_id`, must not be `None`")  # noqa: E501

        self._task_definition_id = task_definition_id

    @property
    def task_definition_as_at(self):
        """Gets the task_definition_as_at of this EventHandler.  # noqa: E501

        AsAt of the required task definition  # noqa: E501

        :return: The task_definition_as_at of this EventHandler.  # noqa: E501
        :rtype: datetime
        """
        return self._task_definition_as_at

    @task_definition_as_at.setter
    def task_definition_as_at(self, task_definition_as_at):
        """Sets the task_definition_as_at of this EventHandler.

        AsAt of the required task definition  # noqa: E501

        :param task_definition_as_at: The task_definition_as_at of this EventHandler.  # noqa: E501
        :type task_definition_as_at: datetime
        """

        self._task_definition_as_at = task_definition_as_at

    @property
    def task_activity(self):
        """Gets the task_activity of this EventHandler.  # noqa: E501


        :return: The task_activity of this EventHandler.  # noqa: E501
        :rtype: lusid_workflow.TaskActivityResponse
        """
        return self._task_activity

    @task_activity.setter
    def task_activity(self, task_activity):
        """Sets the task_activity of this EventHandler.


        :param task_activity: The task_activity of this EventHandler.  # noqa: E501
        :type task_activity: lusid_workflow.TaskActivityResponse
        """
        if self.local_vars_configuration.client_side_validation and task_activity is None:  # noqa: E501
            raise ValueError("Invalid value for `task_activity`, must not be `None`")  # noqa: E501

        self._task_activity = task_activity

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
        if not isinstance(other, EventHandler):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventHandler):
            return True

        return self.to_dict() != other.to_dict()
