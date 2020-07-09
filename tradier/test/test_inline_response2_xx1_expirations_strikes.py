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
from tradier.models.inline_response2_xx1_expirations_strikes import InlineResponse2XX1ExpirationsStrikes  # noqa: E501
from tradier.rest import ApiException

class TestInlineResponse2XX1ExpirationsStrikes(unittest.TestCase):
    """InlineResponse2XX1ExpirationsStrikes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2XX1ExpirationsStrikes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier.models.inline_response2_xx1_expirations_strikes.InlineResponse2XX1ExpirationsStrikes()  # noqa: E501
        if include_optional :
            return InlineResponse2XX1ExpirationsStrikes(
                strike = [
                    1.337
                    ]
            )
        else :
            return InlineResponse2XX1ExpirationsStrikes(
        )

    def testInlineResponse2XX1ExpirationsStrikes(self):
        """Test InlineResponse2XX1ExpirationsStrikes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
