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


class VersionInfo(object):
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
        'as_at_created': 'datetime',
        'user_id_created': 'str',
        'request_id_created': 'str',
        'as_at_modified': 'datetime',
        'user_id_modified': 'str',
        'request_id_modified': 'str',
        'as_at_version_number': 'int'
    }

    attribute_map = {
        'as_at_created': 'asAtCreated',
        'user_id_created': 'userIdCreated',
        'request_id_created': 'requestIdCreated',
        'as_at_modified': 'asAtModified',
        'user_id_modified': 'userIdModified',
        'request_id_modified': 'requestIdModified',
        'as_at_version_number': 'asAtVersionNumber'
    }

    required_map = {
        'as_at_created': 'optional',
        'user_id_created': 'optional',
        'request_id_created': 'optional',
        'as_at_modified': 'optional',
        'user_id_modified': 'optional',
        'request_id_modified': 'optional',
        'as_at_version_number': 'optional'
    }

    def __init__(self, as_at_created=None, user_id_created=None, request_id_created=None, as_at_modified=None, user_id_modified=None, request_id_modified=None, as_at_version_number=None, local_vars_configuration=None):  # noqa: E501
        """VersionInfo - a model defined in OpenAPI"
        
        :param as_at_created:  The asAt datetime at which this entity was first created.
        :type as_at_created: datetime
        :param user_id_created:  The unique id of the user who created this entity.
        :type user_id_created: str
        :param request_id_created:  The request id of the request that created this entity.
        :type request_id_created: str
        :param as_at_modified:  The asAt datetime at which this entity was last updated.
        :type as_at_modified: datetime
        :param user_id_modified:  The unique id of the user who last updated this entity.
        :type user_id_modified: str
        :param request_id_modified:  The request id of the request that last updated this entity.
        :type request_id_modified: str
        :param as_at_version_number:  The integer version number for this entity (the entity was created at version 1).
        :type as_at_version_number: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at_created = None
        self._user_id_created = None
        self._request_id_created = None
        self._as_at_modified = None
        self._user_id_modified = None
        self._request_id_modified = None
        self._as_at_version_number = None
        self.discriminator = None

        self.as_at_created = as_at_created
        self.user_id_created = user_id_created
        self.request_id_created = request_id_created
        self.as_at_modified = as_at_modified
        self.user_id_modified = user_id_modified
        self.request_id_modified = request_id_modified
        self.as_at_version_number = as_at_version_number

    @property
    def as_at_created(self):
        """Gets the as_at_created of this VersionInfo.  # noqa: E501

        The asAt datetime at which this entity was first created.  # noqa: E501

        :return: The as_at_created of this VersionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_created

    @as_at_created.setter
    def as_at_created(self, as_at_created):
        """Sets the as_at_created of this VersionInfo.

        The asAt datetime at which this entity was first created.  # noqa: E501

        :param as_at_created: The as_at_created of this VersionInfo.  # noqa: E501
        :type as_at_created: datetime
        """

        self._as_at_created = as_at_created

    @property
    def user_id_created(self):
        """Gets the user_id_created of this VersionInfo.  # noqa: E501

        The unique id of the user who created this entity.  # noqa: E501

        :return: The user_id_created of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id_created

    @user_id_created.setter
    def user_id_created(self, user_id_created):
        """Sets the user_id_created of this VersionInfo.

        The unique id of the user who created this entity.  # noqa: E501

        :param user_id_created: The user_id_created of this VersionInfo.  # noqa: E501
        :type user_id_created: str
        """

        self._user_id_created = user_id_created

    @property
    def request_id_created(self):
        """Gets the request_id_created of this VersionInfo.  # noqa: E501

        The request id of the request that created this entity.  # noqa: E501

        :return: The request_id_created of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._request_id_created

    @request_id_created.setter
    def request_id_created(self, request_id_created):
        """Sets the request_id_created of this VersionInfo.

        The request id of the request that created this entity.  # noqa: E501

        :param request_id_created: The request_id_created of this VersionInfo.  # noqa: E501
        :type request_id_created: str
        """

        self._request_id_created = request_id_created

    @property
    def as_at_modified(self):
        """Gets the as_at_modified of this VersionInfo.  # noqa: E501

        The asAt datetime at which this entity was last updated.  # noqa: E501

        :return: The as_at_modified of this VersionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_modified

    @as_at_modified.setter
    def as_at_modified(self, as_at_modified):
        """Sets the as_at_modified of this VersionInfo.

        The asAt datetime at which this entity was last updated.  # noqa: E501

        :param as_at_modified: The as_at_modified of this VersionInfo.  # noqa: E501
        :type as_at_modified: datetime
        """

        self._as_at_modified = as_at_modified

    @property
    def user_id_modified(self):
        """Gets the user_id_modified of this VersionInfo.  # noqa: E501

        The unique id of the user who last updated this entity.  # noqa: E501

        :return: The user_id_modified of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id_modified

    @user_id_modified.setter
    def user_id_modified(self, user_id_modified):
        """Sets the user_id_modified of this VersionInfo.

        The unique id of the user who last updated this entity.  # noqa: E501

        :param user_id_modified: The user_id_modified of this VersionInfo.  # noqa: E501
        :type user_id_modified: str
        """

        self._user_id_modified = user_id_modified

    @property
    def request_id_modified(self):
        """Gets the request_id_modified of this VersionInfo.  # noqa: E501

        The request id of the request that last updated this entity.  # noqa: E501

        :return: The request_id_modified of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._request_id_modified

    @request_id_modified.setter
    def request_id_modified(self, request_id_modified):
        """Sets the request_id_modified of this VersionInfo.

        The request id of the request that last updated this entity.  # noqa: E501

        :param request_id_modified: The request_id_modified of this VersionInfo.  # noqa: E501
        :type request_id_modified: str
        """

        self._request_id_modified = request_id_modified

    @property
    def as_at_version_number(self):
        """Gets the as_at_version_number of this VersionInfo.  # noqa: E501

        The integer version number for this entity (the entity was created at version 1).  # noqa: E501

        :return: The as_at_version_number of this VersionInfo.  # noqa: E501
        :rtype: int
        """
        return self._as_at_version_number

    @as_at_version_number.setter
    def as_at_version_number(self, as_at_version_number):
        """Sets the as_at_version_number of this VersionInfo.

        The integer version number for this entity (the entity was created at version 1).  # noqa: E501

        :param as_at_version_number: The as_at_version_number of this VersionInfo.  # noqa: E501
        :type as_at_version_number: int
        """

        self._as_at_version_number = as_at_version_number

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
        if not isinstance(other, VersionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionInfo):
            return True

        return self.to_dict() != other.to_dict()
