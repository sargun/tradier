# coding: utf-8

"""
    Tradier API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tradier_urllib3
from tradier_urllib3.models.inline_response2_xx5_history_day import InlineResponse2XX5HistoryDay  # noqa: E501
from tradier_urllib3.rest import ApiException

class TestInlineResponse2XX5HistoryDay(unittest.TestCase):
    """InlineResponse2XX5HistoryDay unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2XX5HistoryDay
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier_urllib3.models.inline_response2_xx5_history_day.InlineResponse2XX5HistoryDay()  # noqa: E501
        if include_optional :
            return InlineResponse2XX5HistoryDay(
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                open = 1.337, 
                high = 1.337, 
                low = 1.337, 
                close = 1.337, 
                volume = 1.337
            )
        else :
            return InlineResponse2XX5HistoryDay(
        )

    def testInlineResponse2XX5HistoryDay(self):
        """Test InlineResponse2XX5HistoryDay"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
