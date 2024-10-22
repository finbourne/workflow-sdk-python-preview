# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1290
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


class ActionLogOrigin(object):
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
        'task_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'task_id': 'taskId',
        'request_id': 'requestId'
    }

    required_map = {
        'task_id': 'optional',
        'request_id': 'required'
    }

    def __init__(self, task_id=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """ActionLogOrigin - a model defined in OpenAPI"
        
        :param task_id:  The Id of the Task that created this Action
        :type task_id: str
        :param request_id:  The request Id of the request that caused this Action to be triggered.  This could be the original request that caused a sequence of Actions that resulted in this Action (required)
        :type request_id: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._task_id = None
        self._request_id = None
        self.discriminator = None

        self.task_id = task_id
        self.request_id = request_id

    @property
    def task_id(self):
        """Gets the task_id of this ActionLogOrigin.  # noqa: E501

        The Id of the Task that created this Action  # noqa: E501

        :return: The task_id of this ActionLogOrigin.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ActionLogOrigin.

        The Id of the Task that created this Action  # noqa: E501

        :param task_id: The task_id of this ActionLogOrigin.  # noqa: E501
        :type task_id: str
        """

        self._task_id = task_id

    @property
    def request_id(self):
        """Gets the request_id of this ActionLogOrigin.  # noqa: E501

        The request Id of the request that caused this Action to be triggered.  This could be the original request that caused a sequence of Actions that resulted in this Action  # noqa: E501

        :return: The request_id of this ActionLogOrigin.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ActionLogOrigin.

        The request Id of the request that caused this Action to be triggered.  This could be the original request that caused a sequence of Actions that resulted in this Action  # noqa: E501

        :param request_id: The request_id of this ActionLogOrigin.  # noqa: E501
        :type request_id: str
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and len(request_id) < 1):
            raise ValueError("Invalid value for `request_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._request_id = request_id

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
        if not isinstance(other, ActionLogOrigin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionLogOrigin):
            return True

        return self.to_dict() != other.to_dict()
