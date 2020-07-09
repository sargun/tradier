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

import tradier_python
from tradier_python.models.inline_response2_xx1_expirations_expiration import InlineResponse2XX1ExpirationsExpiration  # noqa: E501
from tradier_python.rest import ApiException

class TestInlineResponse2XX1ExpirationsExpiration(unittest.TestCase):
    """InlineResponse2XX1ExpirationsExpiration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2XX1ExpirationsExpiration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier_python.models.inline_response2_xx1_expirations_expiration.InlineResponse2XX1ExpirationsExpiration()  # noqa: E501
        if include_optional :
            return InlineResponse2XX1ExpirationsExpiration(
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                strikes = tradier_python.models.inline_response_2_xx_1_expirations_strikes.inline_response_2XX_1_expirations_strikes(
                    strike = [
                        1.337
                        ], )
            )
        else :
            return InlineResponse2XX1ExpirationsExpiration(
        )

    def testInlineResponse2XX1ExpirationsExpiration(self):
        """Test InlineResponse2XX1ExpirationsExpiration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()