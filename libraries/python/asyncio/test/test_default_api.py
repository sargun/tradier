# coding: utf-8

"""
    Tradier API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tradier_asyncio
from tradier_asyncio.api.default_api import DefaultApi  # noqa: E501
from tradier_asyncio.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = tradier_asyncio.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_markets_events_session_post(self):
        """Test case for markets_events_session_post

        """
        pass

    def test_markets_history_get(self):
        """Test case for markets_history_get

        """
        pass

    def test_markets_options_chains_get(self):
        """Test case for markets_options_chains_get

        """
        pass

    def test_markets_options_expirations_get(self):
        """Test case for markets_options_expirations_get

        """
        pass

    def test_markets_options_lookup_get(self):
        """Test case for markets_options_lookup_get

        """
        pass

    def test_markets_options_strikes_get(self):
        """Test case for markets_options_strikes_get

        """
        pass

    def test_markets_quotes_get(self):
        """Test case for markets_quotes_get

        """
        pass

    def test_markets_quotes_post(self):
        """Test case for markets_quotes_post

        """
        pass

    def test_user_profile_get(self):
        """Test case for user_profile_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
