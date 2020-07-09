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
from tradier.models.inline_response2_xx4_stream import InlineResponse2XX4Stream  # noqa: E501
from tradier.rest import ApiException

class TestInlineResponse2XX4Stream(unittest.TestCase):
    """InlineResponse2XX4Stream unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2XX4Stream
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier.models.inline_response2_xx4_stream.InlineResponse2XX4Stream()  # noqa: E501
        if include_optional :
            return InlineResponse2XX4Stream(
                url = '0', 
                sessionid = '0'
            )
        else :
            return InlineResponse2XX4Stream(
        )

    def testInlineResponse2XX4Stream(self):
        """Test InlineResponse2XX4Stream"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
