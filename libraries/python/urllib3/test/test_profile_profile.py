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
from tradier_urllib3.models.profile_profile import ProfileProfile  # noqa: E501
from tradier_urllib3.rest import ApiException

class TestProfileProfile(unittest.TestCase):
    """ProfileProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProfileProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier_urllib3.models.profile_profile.ProfileProfile()  # noqa: E501
        if include_optional :
            return ProfileProfile(
                account = [
                    tradier_urllib3.models.profile_profile_account.profile_profile_account(
                        account_number = '0', 
                        classification = '0', 
                        day_trader = True, )
                    ]
            )
        else :
            return ProfileProfile(
        )

    def testProfileProfile(self):
        """Test ProfileProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
