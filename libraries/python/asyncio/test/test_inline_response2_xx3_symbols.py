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

import tradier_asyncio
from tradier_asyncio.models.inline_response2_xx3_symbols import InlineResponse2XX3Symbols  # noqa: E501
from tradier_asyncio.rest import ApiException

class TestInlineResponse2XX3Symbols(unittest.TestCase):
    """InlineResponse2XX3Symbols unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2XX3Symbols
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier_asyncio.models.inline_response2_xx3_symbols.InlineResponse2XX3Symbols()  # noqa: E501
        if include_optional :
            return InlineResponse2XX3Symbols(
                root_symbol = '0', 
                options = [
                    '0'
                    ]
            )
        else :
            return InlineResponse2XX3Symbols(
        )

    def testInlineResponse2XX3Symbols(self):
        """Test InlineResponse2XX3Symbols"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
