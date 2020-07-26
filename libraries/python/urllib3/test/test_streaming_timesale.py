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
from tradier_urllib3.models.streaming_timesale import StreamingTimesale  # noqa: E501
from tradier_urllib3.rest import ApiException

class TestStreamingTimesale(unittest.TestCase):
    """StreamingTimesale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StreamingTimesale
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tradier_urllib3.models.streaming_timesale.StreamingTimesale()  # noqa: E501
        if include_optional :
            return StreamingTimesale(
                symbol = '0', 
                exch = '0', 
                bid = 1, 
                ask = 1, 
                last = 1, 
                size = 1, 
                date = 'a', 
                seq = 1.337, 
                flag = '0', 
                cancel = True, 
                correction = True, 
                session = '0'
            )
        else :
            return StreamingTimesale(
        )

    def testStreamingTimesale(self):
        """Test StreamingTimesale"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()