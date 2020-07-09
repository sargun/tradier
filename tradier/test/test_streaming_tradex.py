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

import tradier
from tradier.models.streaming_tradex import StreamingTradex  # noqa: E501
from tradier.rest import ApiException

class TestStreamingTradex(unittest.TestCase):
    """StreamingTradex unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StreamingTradex
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier.models.streaming_tradex.StreamingTradex()  # noqa: E501
        if include_optional :
            return StreamingTradex(
                cvol = 'a', 
                date = 'a', 
                last = '0', 
                price = '0', 
                size = '0', 
                exch = '0', 
                symbol = '0', 
                type = '0'
            )
        else :
            return StreamingTradex(
        )

    def testStreamingTradex(self):
        """Test StreamingTradex"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
