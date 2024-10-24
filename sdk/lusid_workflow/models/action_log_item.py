# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1297
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


class ActionLogItem(object):
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
        'timestamp': 'datetime',
        'log_type': 'str',
        'details': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'log_type': 'logType',
        'details': 'details'
    }

    required_map = {
        'timestamp': 'required',
        'log_type': 'required',
        'details': 'optional'
    }

    def __init__(self, timestamp=None, log_type=None, details=None, local_vars_configuration=None):  # noqa: E501
        """ActionLogItem - a model defined in OpenAPI"
        
        :param timestamp:  The timestamp of the log item (required)
        :type timestamp: datetime
        :param log_type:  The type of log item (required)
        :type log_type: str
        :param details:  The details of the log item
        :type details: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._log_type = None
        self._details = None
        self.discriminator = None

        self.timestamp = timestamp
        self.log_type = log_type
        self.details = details

    @property
    def timestamp(self):
        """Gets the timestamp of this ActionLogItem.  # noqa: E501

        The timestamp of the log item  # noqa: E501

        :return: The timestamp of this ActionLogItem.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ActionLogItem.

        The timestamp of the log item  # noqa: E501

        :param timestamp: The timestamp of this ActionLogItem.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def log_type(self):
        """Gets the log_type of this ActionLogItem.  # noqa: E501

        The type of log item  # noqa: E501

        :return: The log_type of this ActionLogItem.  # noqa: E501
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this ActionLogItem.

        The type of log item  # noqa: E501

        :param log_type: The log_type of this ActionLogItem.  # noqa: E501
        :type log_type: str
        """
        if self.local_vars_configuration.client_side_validation and log_type is None:  # noqa: E501
            raise ValueError("Invalid value for `log_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                log_type is not None and len(log_type) < 1):
            raise ValueError("Invalid value for `log_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._log_type = log_type

    @property
    def details(self):
        """Gets the details of this ActionLogItem.  # noqa: E501

        The details of the log item  # noqa: E501

        :return: The details of this ActionLogItem.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ActionLogItem.

        The details of the log item  # noqa: E501

        :param details: The details of this ActionLogItem.  # noqa: E501
        :type details: str
        """

        self._details = details

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
        if not isinstance(other, ActionLogItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionLogItem):
            return True

        return self.to_dict() != other.to_dict()
