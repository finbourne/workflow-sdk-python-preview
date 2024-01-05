# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.706
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


class GetWorkerResultResponse(object):
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
        'worker_status': 'str',
        'results': 'list[dict[str, object]]',
        'status_detail': 'str'
    }

    attribute_map = {
        'worker_status': 'workerStatus',
        'results': 'results',
        'status_detail': 'statusDetail'
    }

    required_map = {
        'worker_status': 'required',
        'results': 'required',
        'status_detail': 'optional'
    }

    def __init__(self, worker_status=None, results=None, status_detail=None, local_vars_configuration=None):  # noqa: E501
        """GetWorkerResultResponse - a model defined in OpenAPI"
        
        :param worker_status:  The final status of the Worker (required)
        :type worker_status: str
        :param results:  Results (required)
        :type results: list[dict[str, object]]
        :param status_detail:  Detail on the final status
        :type status_detail: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._worker_status = None
        self._results = None
        self._status_detail = None
        self.discriminator = None

        self.worker_status = worker_status
        self.results = results
        self.status_detail = status_detail

    @property
    def worker_status(self):
        """Gets the worker_status of this GetWorkerResultResponse.  # noqa: E501

        The final status of the Worker  # noqa: E501

        :return: The worker_status of this GetWorkerResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._worker_status

    @worker_status.setter
    def worker_status(self, worker_status):
        """Sets the worker_status of this GetWorkerResultResponse.

        The final status of the Worker  # noqa: E501

        :param worker_status: The worker_status of this GetWorkerResultResponse.  # noqa: E501
        :type worker_status: str
        """
        if self.local_vars_configuration.client_side_validation and worker_status is None:  # noqa: E501
            raise ValueError("Invalid value for `worker_status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                worker_status is not None and len(worker_status) < 1):
            raise ValueError("Invalid value for `worker_status`, length must be greater than or equal to `1`")  # noqa: E501

        self._worker_status = worker_status

    @property
    def results(self):
        """Gets the results of this GetWorkerResultResponse.  # noqa: E501

        Results  # noqa: E501

        :return: The results of this GetWorkerResultResponse.  # noqa: E501
        :rtype: list[dict[str, object]]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this GetWorkerResultResponse.

        Results  # noqa: E501

        :param results: The results of this GetWorkerResultResponse.  # noqa: E501
        :type results: list[dict[str, object]]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def status_detail(self):
        """Gets the status_detail of this GetWorkerResultResponse.  # noqa: E501

        Detail on the final status  # noqa: E501

        :return: The status_detail of this GetWorkerResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this GetWorkerResultResponse.

        Detail on the final status  # noqa: E501

        :param status_detail: The status_detail of this GetWorkerResultResponse.  # noqa: E501
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
        if not isinstance(other, GetWorkerResultResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetWorkerResultResponse):
            return True

        return self.to_dict() != other.to_dict()
