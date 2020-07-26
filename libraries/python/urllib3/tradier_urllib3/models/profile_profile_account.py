# coding: utf-8

"""
    Tradier API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tradier_urllib3.configuration import Configuration


class ProfileProfileAccount(object):
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
    """
    openapi_types = {
        'account_number': 'str',
        'classification': 'str',
        'day_trader': 'bool'
    }

    attribute_map = {
        'account_number': 'account_number',
        'classification': 'classification',
        'day_trader': 'day_trader'
    }

    def __init__(self, account_number=None, classification=None, day_trader=None, local_vars_configuration=None):  # noqa: E501
        """ProfileProfileAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_number = None
        self._classification = None
        self._day_trader = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if classification is not None:
            self.classification = classification
        if day_trader is not None:
            self.day_trader = day_trader

    @property
    def account_number(self):
        """Gets the account_number of this ProfileProfileAccount.  # noqa: E501


        :return: The account_number of this ProfileProfileAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ProfileProfileAccount.


        :param account_number: The account_number of this ProfileProfileAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def classification(self):
        """Gets the classification of this ProfileProfileAccount.  # noqa: E501


        :return: The classification of this ProfileProfileAccount.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this ProfileProfileAccount.


        :param classification: The classification of this ProfileProfileAccount.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def day_trader(self):
        """Gets the day_trader of this ProfileProfileAccount.  # noqa: E501


        :return: The day_trader of this ProfileProfileAccount.  # noqa: E501
        :rtype: bool
        """
        return self._day_trader

    @day_trader.setter
    def day_trader(self, day_trader):
        """Sets the day_trader of this ProfileProfileAccount.


        :param day_trader: The day_trader of this ProfileProfileAccount.  # noqa: E501
        :type: bool
        """

        self._day_trader = day_trader

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProfileProfileAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfileProfileAccount):
            return True

        return self.to_dict() != other.to_dict()
