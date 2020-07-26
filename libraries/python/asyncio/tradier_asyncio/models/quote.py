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


class Quote(object):
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
        'symbol': 'str',
        'description': 'str',
        'exch': 'str',
        'type': 'str',
        'last': 'float',
        'change': 'float',
        'volume': 'float',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'bid': 'float',
        'ask': 'float',
        'change_percentage': 'float',
        'average_volume': 'float',
        'last_volume': 'float',
        'trade_date': 'float',
        'prevclose': 'float',
        'week_52_high': 'float',
        'week_52_low': 'float',
        'bidsize': 'float',
        'bidexch': 'str',
        'bid_date': 'float',
        'asksize': 'float',
        'askexch': 'str',
        'ask_date': 'float',
        'root_symbols': 'str',
        'root_symbol': 'str',
        'underlying': 'str',
        'strike': 'float',
        'open_interest': 'float',
        'contract_size': 'float',
        'expiration_date': 'date',
        'expiration_type': 'str',
        'option_type': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'description': 'description',
        'exch': 'exch',
        'type': 'type',
        'last': 'last',
        'change': 'change',
        'volume': 'volume',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'bid': 'bid',
        'ask': 'ask',
        'change_percentage': 'change_percentage',
        'average_volume': 'average_volume',
        'last_volume': 'last_volume',
        'trade_date': 'trade_date',
        'prevclose': 'prevclose',
        'week_52_high': 'week_52_high',
        'week_52_low': 'week_52_low',
        'bidsize': 'bidsize',
        'bidexch': 'bidexch',
        'bid_date': 'bid_date',
        'asksize': 'asksize',
        'askexch': 'askexch',
        'ask_date': 'ask_date',
        'root_symbols': 'root_symbols',
        'root_symbol': 'root_symbol',
        'underlying': 'underlying',
        'strike': 'strike',
        'open_interest': 'open_interest',
        'contract_size': 'contract_size',
        'expiration_date': 'expiration_date',
        'expiration_type': 'expiration_type',
        'option_type': 'option_type'
    }

    def __init__(self, symbol=None, description=None, exch=None, type=None, last=None, change=None, volume=None, open=None, high=None, low=None, close=None, bid=None, ask=None, change_percentage=None, average_volume=None, last_volume=None, trade_date=None, prevclose=None, week_52_high=None, week_52_low=None, bidsize=None, bidexch=None, bid_date=None, asksize=None, askexch=None, ask_date=None, root_symbols=None, root_symbol=None, underlying=None, strike=None, open_interest=None, contract_size=None, expiration_date=None, expiration_type=None, option_type=None, local_vars_configuration=None):  # noqa: E501
        """Quote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._description = None
        self._exch = None
        self._type = None
        self._last = None
        self._change = None
        self._volume = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self._bid = None
        self._ask = None
        self._change_percentage = None
        self._average_volume = None
        self._last_volume = None
        self._trade_date = None
        self._prevclose = None
        self._week_52_high = None
        self._week_52_low = None
        self._bidsize = None
        self._bidexch = None
        self._bid_date = None
        self._asksize = None
        self._askexch = None
        self._ask_date = None
        self._root_symbols = None
        self._root_symbol = None
        self._underlying = None
        self._strike = None
        self._open_interest = None
        self._contract_size = None
        self._expiration_date = None
        self._expiration_type = None
        self._option_type = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if description is not None:
            self.description = description
        if exch is not None:
            self.exch = exch
        if type is not None:
            self.type = type
        if last is not None:
            self.last = last
        if change is not None:
            self.change = change
        if volume is not None:
            self.volume = volume
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close
        if bid is not None:
            self.bid = bid
        if ask is not None:
            self.ask = ask
        if change_percentage is not None:
            self.change_percentage = change_percentage
        if average_volume is not None:
            self.average_volume = average_volume
        if last_volume is not None:
            self.last_volume = last_volume
        if trade_date is not None:
            self.trade_date = trade_date
        if prevclose is not None:
            self.prevclose = prevclose
        if week_52_high is not None:
            self.week_52_high = week_52_high
        if week_52_low is not None:
            self.week_52_low = week_52_low
        if bidsize is not None:
            self.bidsize = bidsize
        if bidexch is not None:
            self.bidexch = bidexch
        if bid_date is not None:
            self.bid_date = bid_date
        if asksize is not None:
            self.asksize = asksize
        if askexch is not None:
            self.askexch = askexch
        if ask_date is not None:
            self.ask_date = ask_date
        if root_symbols is not None:
            self.root_symbols = root_symbols
        if root_symbol is not None:
            self.root_symbol = root_symbol
        if underlying is not None:
            self.underlying = underlying
        if strike is not None:
            self.strike = strike
        if open_interest is not None:
            self.open_interest = open_interest
        if contract_size is not None:
            self.contract_size = contract_size
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if expiration_type is not None:
            self.expiration_type = expiration_type
        if option_type is not None:
            self.option_type = option_type

    @property
    def symbol(self):
        """Gets the symbol of this Quote.  # noqa: E501


        :return: The symbol of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Quote.


        :param symbol: The symbol of this Quote.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def description(self):
        """Gets the description of this Quote.  # noqa: E501


        :return: The description of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Quote.


        :param description: The description of this Quote.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def exch(self):
        """Gets the exch of this Quote.  # noqa: E501


        :return: The exch of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._exch

    @exch.setter
    def exch(self, exch):
        """Sets the exch of this Quote.


        :param exch: The exch of this Quote.  # noqa: E501
        :type: str
        """

        self._exch = exch

    @property
    def type(self):
        """Gets the type of this Quote.  # noqa: E501


        :return: The type of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Quote.


        :param type: The type of this Quote.  # noqa: E501
        :type: str
        """
        allowed_values = ["stock", "option", "etf", "index", "mutual_fund"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def last(self):
        """Gets the last of this Quote.  # noqa: E501


        :return: The last of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Quote.


        :param last: The last of this Quote.  # noqa: E501
        :type: float
        """

        self._last = last

    @property
    def change(self):
        """Gets the change of this Quote.  # noqa: E501


        :return: The change of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this Quote.


        :param change: The change of this Quote.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def volume(self):
        """Gets the volume of this Quote.  # noqa: E501


        :return: The volume of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Quote.


        :param volume: The volume of this Quote.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def open(self):
        """Gets the open of this Quote.  # noqa: E501


        :return: The open of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this Quote.


        :param open: The open of this Quote.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this Quote.  # noqa: E501


        :return: The high of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this Quote.


        :param high: The high of this Quote.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this Quote.  # noqa: E501


        :return: The low of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this Quote.


        :param low: The low of this Quote.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def close(self):
        """Gets the close of this Quote.  # noqa: E501


        :return: The close of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this Quote.


        :param close: The close of this Quote.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def bid(self):
        """Gets the bid of this Quote.  # noqa: E501


        :return: The bid of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this Quote.


        :param bid: The bid of this Quote.  # noqa: E501
        :type: float
        """

        self._bid = bid

    @property
    def ask(self):
        """Gets the ask of this Quote.  # noqa: E501


        :return: The ask of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._ask

    @ask.setter
    def ask(self, ask):
        """Sets the ask of this Quote.


        :param ask: The ask of this Quote.  # noqa: E501
        :type: float
        """

        self._ask = ask

    @property
    def change_percentage(self):
        """Gets the change_percentage of this Quote.  # noqa: E501


        :return: The change_percentage of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._change_percentage

    @change_percentage.setter
    def change_percentage(self, change_percentage):
        """Sets the change_percentage of this Quote.


        :param change_percentage: The change_percentage of this Quote.  # noqa: E501
        :type: float
        """

        self._change_percentage = change_percentage

    @property
    def average_volume(self):
        """Gets the average_volume of this Quote.  # noqa: E501


        :return: The average_volume of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._average_volume

    @average_volume.setter
    def average_volume(self, average_volume):
        """Sets the average_volume of this Quote.


        :param average_volume: The average_volume of this Quote.  # noqa: E501
        :type: float
        """

        self._average_volume = average_volume

    @property
    def last_volume(self):
        """Gets the last_volume of this Quote.  # noqa: E501


        :return: The last_volume of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._last_volume

    @last_volume.setter
    def last_volume(self, last_volume):
        """Sets the last_volume of this Quote.


        :param last_volume: The last_volume of this Quote.  # noqa: E501
        :type: float
        """

        self._last_volume = last_volume

    @property
    def trade_date(self):
        """Gets the trade_date of this Quote.  # noqa: E501

        Unix time of trade  # noqa: E501

        :return: The trade_date of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._trade_date

    @trade_date.setter
    def trade_date(self, trade_date):
        """Sets the trade_date of this Quote.

        Unix time of trade  # noqa: E501

        :param trade_date: The trade_date of this Quote.  # noqa: E501
        :type: float
        """

        self._trade_date = trade_date

    @property
    def prevclose(self):
        """Gets the prevclose of this Quote.  # noqa: E501


        :return: The prevclose of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._prevclose

    @prevclose.setter
    def prevclose(self, prevclose):
        """Sets the prevclose of this Quote.


        :param prevclose: The prevclose of this Quote.  # noqa: E501
        :type: float
        """

        self._prevclose = prevclose

    @property
    def week_52_high(self):
        """Gets the week_52_high of this Quote.  # noqa: E501


        :return: The week_52_high of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._week_52_high

    @week_52_high.setter
    def week_52_high(self, week_52_high):
        """Sets the week_52_high of this Quote.


        :param week_52_high: The week_52_high of this Quote.  # noqa: E501
        :type: float
        """

        self._week_52_high = week_52_high

    @property
    def week_52_low(self):
        """Gets the week_52_low of this Quote.  # noqa: E501


        :return: The week_52_low of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._week_52_low

    @week_52_low.setter
    def week_52_low(self, week_52_low):
        """Sets the week_52_low of this Quote.


        :param week_52_low: The week_52_low of this Quote.  # noqa: E501
        :type: float
        """

        self._week_52_low = week_52_low

    @property
    def bidsize(self):
        """Gets the bidsize of this Quote.  # noqa: E501


        :return: The bidsize of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._bidsize

    @bidsize.setter
    def bidsize(self, bidsize):
        """Sets the bidsize of this Quote.


        :param bidsize: The bidsize of this Quote.  # noqa: E501
        :type: float
        """

        self._bidsize = bidsize

    @property
    def bidexch(self):
        """Gets the bidexch of this Quote.  # noqa: E501


        :return: The bidexch of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._bidexch

    @bidexch.setter
    def bidexch(self, bidexch):
        """Sets the bidexch of this Quote.


        :param bidexch: The bidexch of this Quote.  # noqa: E501
        :type: str
        """

        self._bidexch = bidexch

    @property
    def bid_date(self):
        """Gets the bid_date of this Quote.  # noqa: E501

        Unix time of bid  # noqa: E501

        :return: The bid_date of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._bid_date

    @bid_date.setter
    def bid_date(self, bid_date):
        """Sets the bid_date of this Quote.

        Unix time of bid  # noqa: E501

        :param bid_date: The bid_date of this Quote.  # noqa: E501
        :type: float
        """

        self._bid_date = bid_date

    @property
    def asksize(self):
        """Gets the asksize of this Quote.  # noqa: E501


        :return: The asksize of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._asksize

    @asksize.setter
    def asksize(self, asksize):
        """Sets the asksize of this Quote.


        :param asksize: The asksize of this Quote.  # noqa: E501
        :type: float
        """

        self._asksize = asksize

    @property
    def askexch(self):
        """Gets the askexch of this Quote.  # noqa: E501


        :return: The askexch of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._askexch

    @askexch.setter
    def askexch(self, askexch):
        """Sets the askexch of this Quote.


        :param askexch: The askexch of this Quote.  # noqa: E501
        :type: str
        """

        self._askexch = askexch

    @property
    def ask_date(self):
        """Gets the ask_date of this Quote.  # noqa: E501

        Unix time of ask  # noqa: E501

        :return: The ask_date of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._ask_date

    @ask_date.setter
    def ask_date(self, ask_date):
        """Sets the ask_date of this Quote.

        Unix time of ask  # noqa: E501

        :param ask_date: The ask_date of this Quote.  # noqa: E501
        :type: float
        """

        self._ask_date = ask_date

    @property
    def root_symbols(self):
        """Gets the root_symbols of this Quote.  # noqa: E501

        Comma-delimited list of option root symbols for an underlier  # noqa: E501

        :return: The root_symbols of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._root_symbols

    @root_symbols.setter
    def root_symbols(self, root_symbols):
        """Sets the root_symbols of this Quote.

        Comma-delimited list of option root symbols for an underlier  # noqa: E501

        :param root_symbols: The root_symbols of this Quote.  # noqa: E501
        :type: str
        """

        self._root_symbols = root_symbols

    @property
    def root_symbol(self):
        """Gets the root_symbol of this Quote.  # noqa: E501


        :return: The root_symbol of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._root_symbol

    @root_symbol.setter
    def root_symbol(self, root_symbol):
        """Sets the root_symbol of this Quote.


        :param root_symbol: The root_symbol of this Quote.  # noqa: E501
        :type: str
        """

        self._root_symbol = root_symbol

    @property
    def underlying(self):
        """Gets the underlying of this Quote.  # noqa: E501

        Underlying security of the option (if applicable)  # noqa: E501

        :return: The underlying of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this Quote.

        Underlying security of the option (if applicable)  # noqa: E501

        :param underlying: The underlying of this Quote.  # noqa: E501
        :type: str
        """

        self._underlying = underlying

    @property
    def strike(self):
        """Gets the strike of this Quote.  # noqa: E501


        :return: The strike of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this Quote.


        :param strike: The strike of this Quote.  # noqa: E501
        :type: float
        """

        self._strike = strike

    @property
    def open_interest(self):
        """Gets the open_interest of this Quote.  # noqa: E501


        :return: The open_interest of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._open_interest

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this Quote.


        :param open_interest: The open_interest of this Quote.  # noqa: E501
        :type: float
        """

        self._open_interest = open_interest

    @property
    def contract_size(self):
        """Gets the contract_size of this Quote.  # noqa: E501


        :return: The contract_size of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this Quote.


        :param contract_size: The contract_size of this Quote.  # noqa: E501
        :type: float
        """

        self._contract_size = contract_size

    @property
    def expiration_date(self):
        """Gets the expiration_date of this Quote.  # noqa: E501


        :return: The expiration_date of this Quote.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this Quote.


        :param expiration_date: The expiration_date of this Quote.  # noqa: E501
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def expiration_type(self):
        """Gets the expiration_type of this Quote.  # noqa: E501


        :return: The expiration_type of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._expiration_type

    @expiration_type.setter
    def expiration_type(self, expiration_type):
        """Sets the expiration_type of this Quote.


        :param expiration_type: The expiration_type of this Quote.  # noqa: E501
        :type: str
        """

        self._expiration_type = expiration_type

    @property
    def option_type(self):
        """Gets the option_type of this Quote.  # noqa: E501


        :return: The option_type of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this Quote.


        :param option_type: The option_type of this Quote.  # noqa: E501
        :type: str
        """
        allowed_values = ["put", "call"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and option_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `option_type` ({0}), must be one of {1}"  # noqa: E501
                .format(option_type, allowed_values)
            )

        self._option_type = option_type

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
        if not isinstance(other, Quote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quote):
            return True

        return self.to_dict() != other.to_dict()