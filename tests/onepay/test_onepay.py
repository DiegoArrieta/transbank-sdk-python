import unittest

from tbk import onepay

class OnepayTestCase(unittest.TestCase):
    def test_set_global_keys(self):
        onepay.api_key = "api_key"
        onepay.shared_secret = "shared_secret"
        onepay.callback_url = "callback_url"
        onepay.app_scheme = "app_scheme"

        self.assertEqual(onepay.api_key, "api_key")
        self.assertEqual(onepay.shared_secret, "shared_secret")
        self.assertEqual(onepay.callback_url, "callback_url")
        self.assertEqual(onepay.app_scheme, "app_scheme")

    def test_integration_types(self):
        self.assertIsNotNone(onepay.IntegrationType.LIVE)
        self.assertIsNotNone(onepay.IntegrationType.TEST)
        self.assertIsNotNone(onepay.IntegrationType.MOCK)

        self.assertIsNotNone(onepay.IntegrationType.LIVE.value.api_base)
        self.assertIsNotNone(onepay.IntegrationType.LIVE.value.key)
        self.assertIsNotNone(onepay.IntegrationType.LIVE.value.app_key)

        onepay.integration_type = onepay.IntegrationType.LIVE
        self.assertEqual(onepay.integration_type, onepay.IntegrationType.LIVE)
