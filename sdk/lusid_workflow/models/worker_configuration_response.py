# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.808
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


class WorkerConfigurationResponse(object):
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
        'url': 'str',
        'name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url',
        'name': 'name'
    }

    required_map = {
        'type': 'required',
        'url': 'optional',
        'name': 'optional'
    }

    def __init__(self, type=None, url=None, name=None, local_vars_configuration=None):  # noqa: E501
        """WorkerConfigurationResponse - a model defined in OpenAPI"
        
        :param type:  The type of worker (required)
        :type type: str
        :param url:  The URL to check, eg: https://www.google.com/
        :type url: str
        :param name:  Name of the view in Luminesce
        :type name: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._url = None
        self._name = None
        self.discriminator = None

        self.type = type
        self.url = url
        self.name = name

    @property
    def type(self):
        """Gets the type of this WorkerConfigurationResponse.  # noqa: E501

        The type of worker  # noqa: E501

        :return: The type of this WorkerConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkerConfigurationResponse.

        The type of worker  # noqa: E501

        :param type: The type of this WorkerConfigurationResponse.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Sleep"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """Gets the url of this WorkerConfigurationResponse.  # noqa: E501

        The URL to check, eg: https://www.google.com/  # noqa: E501

        :return: The url of this WorkerConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WorkerConfigurationResponse.

        The URL to check, eg: https://www.google.com/  # noqa: E501

        :param url: The url of this WorkerConfigurationResponse.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this WorkerConfigurationResponse.  # noqa: E501

        Name of the view in Luminesce  # noqa: E501

        :return: The name of this WorkerConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkerConfigurationResponse.

        Name of the view in Luminesce  # noqa: E501

        :param name: The name of this WorkerConfigurationResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, WorkerConfigurationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerConfigurationResponse):
            return True

        return self.to_dict() != other.to_dict()
