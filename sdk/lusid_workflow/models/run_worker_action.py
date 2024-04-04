# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.857
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


class RunWorkerAction(object):
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
        'worker_id': 'ResourceId',
        'worker_as_at': 'datetime',
        'worker_parameters': 'dict[str, FieldMapping]',
        'worker_status_triggers': 'WorkerStatusTriggers',
        'child_task_configurations': 'list[ResultantChildTaskConfiguration]'
    }

    attribute_map = {
        'type': 'type',
        'worker_id': 'workerId',
        'worker_as_at': 'workerAsAt',
        'worker_parameters': 'workerParameters',
        'worker_status_triggers': 'workerStatusTriggers',
        'child_task_configurations': 'childTaskConfigurations'
    }

    required_map = {
        'type': 'required',
        'worker_id': 'required',
        'worker_as_at': 'optional',
        'worker_parameters': 'optional',
        'worker_status_triggers': 'optional',
        'child_task_configurations': 'optional'
    }

    def __init__(self, type=None, worker_id=None, worker_as_at=None, worker_parameters=None, worker_status_triggers=None, child_task_configurations=None, local_vars_configuration=None):  # noqa: E501
        """RunWorkerAction - a model defined in OpenAPI"
        
        :param type:  Type name for this Action (required)
        :type type: str
        :param worker_id:  (required)
        :type worker_id: lusid_workflow.ResourceId
        :param worker_as_at:  Worker AsAt
        :type worker_as_at: datetime
        :param worker_parameters:  Parameters for this Worker
        :type worker_parameters: dict[str, lusid_workflow.FieldMapping]
        :param worker_status_triggers: 
        :type worker_status_triggers: lusid_workflow.WorkerStatusTriggers
        :param child_task_configurations:  Tasks can be generated from run worker results; this is the configuration
        :type child_task_configurations: list[lusid_workflow.ResultantChildTaskConfiguration]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._worker_id = None
        self._worker_as_at = None
        self._worker_parameters = None
        self._worker_status_triggers = None
        self._child_task_configurations = None
        self.discriminator = None

        self.type = type
        self.worker_id = worker_id
        self.worker_as_at = worker_as_at
        self.worker_parameters = worker_parameters
        if worker_status_triggers is not None:
            self.worker_status_triggers = worker_status_triggers
        self.child_task_configurations = child_task_configurations

    @property
    def type(self):
        """Gets the type of this RunWorkerAction.  # noqa: E501

        Type name for this Action  # noqa: E501

        :return: The type of this RunWorkerAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RunWorkerAction.

        Type name for this Action  # noqa: E501

        :param type: The type of this RunWorkerAction.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["RunWorker"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def worker_id(self):
        """Gets the worker_id of this RunWorkerAction.  # noqa: E501


        :return: The worker_id of this RunWorkerAction.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this RunWorkerAction.


        :param worker_id: The worker_id of this RunWorkerAction.  # noqa: E501
        :type worker_id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and worker_id is None:  # noqa: E501
            raise ValueError("Invalid value for `worker_id`, must not be `None`")  # noqa: E501

        self._worker_id = worker_id

    @property
    def worker_as_at(self):
        """Gets the worker_as_at of this RunWorkerAction.  # noqa: E501

        Worker AsAt  # noqa: E501

        :return: The worker_as_at of this RunWorkerAction.  # noqa: E501
        :rtype: datetime
        """
        return self._worker_as_at

    @worker_as_at.setter
    def worker_as_at(self, worker_as_at):
        """Sets the worker_as_at of this RunWorkerAction.

        Worker AsAt  # noqa: E501

        :param worker_as_at: The worker_as_at of this RunWorkerAction.  # noqa: E501
        :type worker_as_at: datetime
        """

        self._worker_as_at = worker_as_at

    @property
    def worker_parameters(self):
        """Gets the worker_parameters of this RunWorkerAction.  # noqa: E501

        Parameters for this Worker  # noqa: E501

        :return: The worker_parameters of this RunWorkerAction.  # noqa: E501
        :rtype: dict[str, lusid_workflow.FieldMapping]
        """
        return self._worker_parameters

    @worker_parameters.setter
    def worker_parameters(self, worker_parameters):
        """Sets the worker_parameters of this RunWorkerAction.

        Parameters for this Worker  # noqa: E501

        :param worker_parameters: The worker_parameters of this RunWorkerAction.  # noqa: E501
        :type worker_parameters: dict[str, lusid_workflow.FieldMapping]
        """

        self._worker_parameters = worker_parameters

    @property
    def worker_status_triggers(self):
        """Gets the worker_status_triggers of this RunWorkerAction.  # noqa: E501


        :return: The worker_status_triggers of this RunWorkerAction.  # noqa: E501
        :rtype: lusid_workflow.WorkerStatusTriggers
        """
        return self._worker_status_triggers

    @worker_status_triggers.setter
    def worker_status_triggers(self, worker_status_triggers):
        """Sets the worker_status_triggers of this RunWorkerAction.


        :param worker_status_triggers: The worker_status_triggers of this RunWorkerAction.  # noqa: E501
        :type worker_status_triggers: lusid_workflow.WorkerStatusTriggers
        """

        self._worker_status_triggers = worker_status_triggers

    @property
    def child_task_configurations(self):
        """Gets the child_task_configurations of this RunWorkerAction.  # noqa: E501

        Tasks can be generated from run worker results; this is the configuration  # noqa: E501

        :return: The child_task_configurations of this RunWorkerAction.  # noqa: E501
        :rtype: list[lusid_workflow.ResultantChildTaskConfiguration]
        """
        return self._child_task_configurations

    @child_task_configurations.setter
    def child_task_configurations(self, child_task_configurations):
        """Sets the child_task_configurations of this RunWorkerAction.

        Tasks can be generated from run worker results; this is the configuration  # noqa: E501

        :param child_task_configurations: The child_task_configurations of this RunWorkerAction.  # noqa: E501
        :type child_task_configurations: list[lusid_workflow.ResultantChildTaskConfiguration]
        """

        self._child_task_configurations = child_task_configurations

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
        if not isinstance(other, RunWorkerAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunWorkerAction):
            return True

        return self.to_dict() != other.to_dict()
