import unittest

from transbank import webpay
from transbank.webpay.configuration import Configuration
from transbank.webpay.webpay import *

class WebpayTestCase(unittest.TestCase):
    def test_tests_configurations(self):
        configuration_webpay_normal = Configuration.for_testing_webpay_plus_normal()
        self.assertIsNotNone(configuration_webpay_normal)
        self.assertIsNotNone(configuration_webpay_normal.commerce_code)
        self.assertIsNotNone(configuration_webpay_normal.private_key)
        self.assertIsNotNone(configuration_webpay_normal.public_cert)

        configuration_webpay_capture = Configuration.for_testing_webpay_plus_capture()
        self.assertIsNotNone(configuration_webpay_capture)
        self.assertIsNotNone(configuration_webpay_capture.commerce_code)
        self.assertIsNotNone(configuration_webpay_capture.private_key)
        self.assertIsNotNone(configuration_webpay_capture.public_cert)

        configuration_webpay_mall = Configuration.for_testing_webpay_plus_mall()
        self.assertIsNotNone(configuration_webpay_mall)
        self.assertIsNotNone(configuration_webpay_mall.commerce_code)
        self.assertIsNotNone(configuration_webpay_mall.private_key)
        self.assertIsNotNone(configuration_webpay_mall.public_cert)

        configuration_oneclick_normal = Configuration.for_testing_webpay_oneclick_normal()
        self.assertIsNotNone(configuration_oneclick_normal)
        self.assertIsNotNone(configuration_oneclick_normal.commerce_code)
        self.assertIsNotNone(configuration_oneclick_normal.private_key)
        self.assertIsNotNone(configuration_oneclick_normal.public_cert)

        configuration_patpass_normal = Configuration.for_testing_patpass_by_webpay_normal("transbank@patpass.cl")
        self.assertIsNotNone(configuration_patpass_normal)
        self.assertIsNotNone(configuration_patpass_normal.commerce_code)
        self.assertIsNotNone(configuration_patpass_normal.private_key)
        self.assertIsNotNone(configuration_patpass_normal.public_cert)

    def test_init_transaction_webpay_normal(self):
        transaction = Webpay(Configuration.for_testing_webpay_plus_normal()).get_normal_transaction()
        result = transaction.init_transaction(1000, 100001, "mi-id-de-sesion", "https://callback/resultado/de/transaccion", "https://callback/final/post/comprobante/webpay")
        self.assertIsNotNone(result['url'])
        self.assertIsNotNone(result['token'])
        print(result['token'])

    def test_transaction_result_webpay_normal(self):
        transaction = Webpay(Configuration.for_testing_webpay_plus_normal()).get_normal_transaction()
        result = transaction.get_transaction_result("e9ddbc3a8ae754b232bb99f13b4d76e25e35b629738d8eb06961db7e1fe3ce0e")
        self.assertIsNotNone(result['detailOutput'][0])
        self.assertIsNotNone(result['detailOutput'][0]['responseCode'])
        print(result)

