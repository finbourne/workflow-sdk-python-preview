# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1158
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


class ResultMatchingPattern(object):
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
        'filter': 'str'
    }

    attribute_map = {
        'filter': 'filter'
    }

    required_map = {
        'filter': 'required'
    }

    def __init__(self, filter=None, local_vars_configuration=None):  # noqa: E501
        """ResultMatchingPattern - a model defined in OpenAPI"
        
        :param filter:  Filter string (required)
        :type filter: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self.discriminator = None

        self.filter = filter

    @property
    def filter(self):
        """Gets the filter of this ResultMatchingPattern.  # noqa: E501

        Filter string  # noqa: E501

        :return: The filter of this ResultMatchingPattern.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ResultMatchingPattern.

        Filter string  # noqa: E501

        :param filter: The filter of this ResultMatchingPattern.  # noqa: E501
        :type filter: str
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) > 1024):
            raise ValueError("Invalid value for `filter`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) < 1):
            raise ValueError("Invalid value for `filter`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and not re.search(r'^[\s\S]*$', filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._filter = filter

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
        if not isinstance(other, ResultMatchingPattern):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultMatchingPattern):
            return True

        return self.to_dict() != other.to_dict()
