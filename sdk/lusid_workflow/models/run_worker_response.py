# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1026
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


class RunWorkerResponse(object):
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
        'run_id': 'int',
        'status_detail': 'str'
    }

    attribute_map = {
        'run_id': 'runId',
        'status_detail': 'statusDetail'
    }

    required_map = {
        'run_id': 'required',
        'status_detail': 'optional'
    }

    def __init__(self, run_id=None, status_detail=None, local_vars_configuration=None):  # noqa: E501
        """RunWorkerResponse - a model defined in OpenAPI"
        
        :param run_id:  Identifies a Worker run (required)
        :type run_id: int
        :param status_detail:  Detail on the final status
        :type status_detail: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._status_detail = None
        self.discriminator = None

        self.run_id = run_id
        self.status_detail = status_detail

    @property
    def run_id(self):
        """Gets the run_id of this RunWorkerResponse.  # noqa: E501

        Identifies a Worker run  # noqa: E501

        :return: The run_id of this RunWorkerResponse.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this RunWorkerResponse.

        Identifies a Worker run  # noqa: E501

        :param run_id: The run_id of this RunWorkerResponse.  # noqa: E501
        :type run_id: int
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def status_detail(self):
        """Gets the status_detail of this RunWorkerResponse.  # noqa: E501

        Detail on the final status  # noqa: E501

        :return: The status_detail of this RunWorkerResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this RunWorkerResponse.

        Detail on the final status  # noqa: E501

        :param status_detail: The status_detail of this RunWorkerResponse.  # noqa: E501
        :type status_detail: str
        """

        self._status_detail = status_detail

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
        if not isinstance(other, RunWorkerResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunWorkerResponse):
            return True

        return self.to_dict() != other.to_dict()
