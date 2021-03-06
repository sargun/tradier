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

from tradier_asyncio.configuration import Configuration


class StreamingQuote(object):
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
        'ask': 'float',
        'askdate': 'str',
        'askexch': 'str',
        'asksz': 'float',
        'bid': 'float',
        'biddate': 'str',
        'bidexch': 'str',
        'symbol': 'str',
        'type': 'str'
    }

    attribute_map = {
        'ask': 'ask',
        'askdate': 'askdate',
        'askexch': 'askexch',
        'asksz': 'asksz',
        'bid': 'bid',
        'biddate': 'biddate',
        'bidexch': 'bidexch',
        'symbol': 'symbol',
        'type': 'type'
    }

    def __init__(self, ask=None, askdate=None, askexch=None, asksz=None, bid=None, biddate=None, bidexch=None, symbol=None, type=None, local_vars_configuration=None):  # noqa: E501
        """StreamingQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ask = None
        self._askdate = None
        self._askexch = None
        self._asksz = None
        self._bid = None
        self._biddate = None
        self._bidexch = None
        self._symbol = None
        self._type = None
        self.discriminator = None

        if ask is not None:
            self.ask = ask
        if askdate is not None:
            self.askdate = askdate
        if askexch is not None:
            self.askexch = askexch
        if asksz is not None:
            self.asksz = asksz
        if bid is not None:
            self.bid = bid
        if biddate is not None:
            self.biddate = biddate
        if bidexch is not None:
            self.bidexch = bidexch
        if symbol is not None:
            self.symbol = symbol
        if type is not None:
            self.type = type

    @property
    def ask(self):
        """Gets the ask of this StreamingQuote.  # noqa: E501


        :return: The ask of this StreamingQuote.  # noqa: E501
        :rtype: float
        """
        return self._ask

    @ask.setter
    def ask(self, ask):
        """Sets the ask of this StreamingQuote.


        :param ask: The ask of this StreamingQuote.  # noqa: E501
        :type: float
        """

        self._ask = ask

    @property
    def askdate(self):
        """Gets the askdate of this StreamingQuote.  # noqa: E501


        :return: The askdate of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._askdate

    @askdate.setter
    def askdate(self, askdate):
        """Sets the askdate of this StreamingQuote.


        :param askdate: The askdate of this StreamingQuote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                askdate is not None and not re.search(r'^[0-9]+$', askdate)):  # noqa: E501
            raise ValueError(r"Invalid value for `askdate`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._askdate = askdate

    @property
    def askexch(self):
        """Gets the askexch of this StreamingQuote.  # noqa: E501


        :return: The askexch of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._askexch

    @askexch.setter
    def askexch(self, askexch):
        """Sets the askexch of this StreamingQuote.


        :param askexch: The askexch of this StreamingQuote.  # noqa: E501
        :type: str
        """

        self._askexch = askexch

    @property
    def asksz(self):
        """Gets the asksz of this StreamingQuote.  # noqa: E501


        :return: The asksz of this StreamingQuote.  # noqa: E501
        :rtype: float
        """
        return self._asksz

    @asksz.setter
    def asksz(self, asksz):
        """Sets the asksz of this StreamingQuote.


        :param asksz: The asksz of this StreamingQuote.  # noqa: E501
        :type: float
        """

        self._asksz = asksz

    @property
    def bid(self):
        """Gets the bid of this StreamingQuote.  # noqa: E501


        :return: The bid of this StreamingQuote.  # noqa: E501
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this StreamingQuote.


        :param bid: The bid of this StreamingQuote.  # noqa: E501
        :type: float
        """

        self._bid = bid

    @property
    def biddate(self):
        """Gets the biddate of this StreamingQuote.  # noqa: E501


        :return: The biddate of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._biddate

    @biddate.setter
    def biddate(self, biddate):
        """Sets the biddate of this StreamingQuote.


        :param biddate: The biddate of this StreamingQuote.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                biddate is not None and not re.search(r'^[0-9]+$', biddate)):  # noqa: E501
            raise ValueError(r"Invalid value for `biddate`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._biddate = biddate

    @property
    def bidexch(self):
        """Gets the bidexch of this StreamingQuote.  # noqa: E501


        :return: The bidexch of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._bidexch

    @bidexch.setter
    def bidexch(self, bidexch):
        """Sets the bidexch of this StreamingQuote.


        :param bidexch: The bidexch of this StreamingQuote.  # noqa: E501
        :type: str
        """

        self._bidexch = bidexch

    @property
    def symbol(self):
        """Gets the symbol of this StreamingQuote.  # noqa: E501


        :return: The symbol of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this StreamingQuote.


        :param symbol: The symbol of this StreamingQuote.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def type(self):
        """Gets the type of this StreamingQuote.  # noqa: E501


        :return: The type of this StreamingQuote.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StreamingQuote.


        :param type: The type of this StreamingQuote.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, StreamingQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamingQuote):
            return True

        return self.to_dict() != other.to_dict()
