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

from tradier.configuration import Configuration


class InlineResponse2XX5HistoryDay(object):
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
        'date': 'date',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'float'
    }

    attribute_map = {
        'date': 'date',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'volume': 'volume'
    }

    def __init__(self, date=None, open=None, high=None, low=None, close=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2XX5HistoryDay - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self._volume = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close
        if volume is not None:
            self.volume = volume

    @property
    def date(self):
        """Gets the date of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The date of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InlineResponse2XX5HistoryDay.


        :param date: The date of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def open(self):
        """Gets the open of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The open of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this InlineResponse2XX5HistoryDay.


        :param open: The open of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The high of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this InlineResponse2XX5HistoryDay.


        :param high: The high of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The low of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this InlineResponse2XX5HistoryDay.


        :param low: The low of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def close(self):
        """Gets the close of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The close of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this InlineResponse2XX5HistoryDay.


        :param close: The close of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def volume(self):
        """Gets the volume of this InlineResponse2XX5HistoryDay.  # noqa: E501


        :return: The volume of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InlineResponse2XX5HistoryDay.


        :param volume: The volume of this InlineResponse2XX5HistoryDay.  # noqa: E501
        :type: float
        """

        self._volume = volume

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
        if not isinstance(other, InlineResponse2XX5HistoryDay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2XX5HistoryDay):
            return True

        return self.to_dict() != other.to_dict()
