# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.157
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


class TriggerInvocationResponse(object):
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
        'was_successful': 'bool',
        'as_at': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'was_successful': 'wasSuccessful',
        'as_at': 'asAt',
        'message': 'message'
    }

    required_map = {
        'was_successful': 'optional',
        'as_at': 'optional',
        'message': 'optional'
    }

    def __init__(self, was_successful=None, as_at=None, message=None, local_vars_configuration=None):  # noqa: E501
        """TriggerInvocationResponse - a model defined in OpenAPI"
        
        :param was_successful:  A flag indicating success
        :type was_successful: bool
        :param as_at:  If successful, the AsAt time
        :type as_at: datetime
        :param message:  Any messaging
        :type message: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._was_successful = None
        self._as_at = None
        self._message = None
        self.discriminator = None

        if was_successful is not None:
            self.was_successful = was_successful
        self.as_at = as_at
        self.message = message

    @property
    def was_successful(self):
        """Gets the was_successful of this TriggerInvocationResponse.  # noqa: E501

        A flag indicating success  # noqa: E501

        :return: The was_successful of this TriggerInvocationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._was_successful

    @was_successful.setter
    def was_successful(self, was_successful):
        """Sets the was_successful of this TriggerInvocationResponse.

        A flag indicating success  # noqa: E501

        :param was_successful: The was_successful of this TriggerInvocationResponse.  # noqa: E501
        :type was_successful: bool
        """

        self._was_successful = was_successful

    @property
    def as_at(self):
        """Gets the as_at of this TriggerInvocationResponse.  # noqa: E501

        If successful, the AsAt time  # noqa: E501

        :return: The as_at of this TriggerInvocationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this TriggerInvocationResponse.

        If successful, the AsAt time  # noqa: E501

        :param as_at: The as_at of this TriggerInvocationResponse.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def message(self):
        """Gets the message of this TriggerInvocationResponse.  # noqa: E501

        Any messaging  # noqa: E501

        :return: The message of this TriggerInvocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TriggerInvocationResponse.

        Any messaging  # noqa: E501

        :param message: The message of this TriggerInvocationResponse.  # noqa: E501
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, TriggerInvocationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TriggerInvocationResponse):
            return True

        return self.to_dict() != other.to_dict()
