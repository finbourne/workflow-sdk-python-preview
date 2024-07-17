# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1172
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


class RunWorkerRequest(object):
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
        'parameters': 'list[ParameterValue]'
    }

    attribute_map = {
        'parameters': 'parameters'
    }

    required_map = {
        'parameters': 'required'
    }

    def __init__(self, parameters=None, local_vars_configuration=None):  # noqa: E501
        """RunWorkerRequest - a model defined in OpenAPI"
        
        :param parameters:  The Parameter and their values. (required)
        :type parameters: list[lusid_workflow.ParameterValue]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._parameters = None
        self.discriminator = None

        self.parameters = parameters

    @property
    def parameters(self):
        """Gets the parameters of this RunWorkerRequest.  # noqa: E501

        The Parameter and their values.  # noqa: E501

        :return: The parameters of this RunWorkerRequest.  # noqa: E501
        :rtype: list[lusid_workflow.ParameterValue]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this RunWorkerRequest.

        The Parameter and their values.  # noqa: E501

        :param parameters: The parameters of this RunWorkerRequest.  # noqa: E501
        :type parameters: list[lusid_workflow.ParameterValue]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, RunWorkerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunWorkerRequest):
            return True

        return self.to_dict() != other.to_dict()
